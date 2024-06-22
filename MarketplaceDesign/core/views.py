from django.shortcuts import render, redirect, get_object_or_404
from .models import Good, Cart, CartItem
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.db.models import Q
from decimal import Decimal


def search_view(request):
    query = request.GET.get('query')
    user_query = None
    if query:
        user_query = Good.objects.filter(Q(name__icontains=query))
        print(user_query)
    context = {
        'user_query': user_query
    }
    return render(request, 'core/MainPage.html', context)


def main_page(request):
    query = request.GET.get('query')
    user_query = None
    search = False
    if query:
        user_query = Good.objects.filter(Q(name__icontains=query))[:8]
        search = True
    context = {
        "user_query": user_query,
        "search": search
    }
    return render(request, 'core/MainPage.html', context)


def catalog(request):
    goods = Good.objects.all()
    return render(request, 'core/CatalogPage.html', {'goods': goods})


def good_info(request, pk):
    good = get_object_or_404(Good, pk=pk)
    return render(request, 'core/GoodInfoPage.html', {'good': good})


# @login_required
# @require_POST
# def add_in_cart(request, pk):
#     try:
#         user_cart = Cart.objects.get(user=request.user)
#         print("Корзина есть")
#     except Cart.DoesNotExist:
#         print("Корзины нет")
#         user_cart = Cart.objects.create(user=request.user)
#     good = Good.objects.get(id=pk)
#     user_cart.total_products = F('total_products') + 1
#     user_cart.save()
#     user_cart.goods_in_cart.add(good)
#     return redirect('Cart')
#
#
# @login_required
# def cart(request):
#     try:
#         user_cart = Cart.objects.filter(user=request.user)
#     except TypeError:
#         print("Карзина пуста")
#         user_cart = None
#     return render(request, "core/CartPage.html", {"cart": user_cart})

@login_required
@require_POST
def add_in_cart(request, pk):
    good = get_object_or_404(Good, pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user, in_order=False)

    # Проверяем, есть ли уже такой товар в корзине пользователя
    cart_item, created = CartItem.objects.get_or_create(cart=cart, good=good)
    cart_item.quantity += 1
    cart_item.save()

    # Обновляем общее количество товаров и общую стоимость корзины
    cart.total_products += 1
    cart.final_price += Decimal(good.price)
    cart.save()

    return redirect('Cart')

@login_required
def cart(request):
    try:
        user_cart = Cart.objects.get(user=request.user, in_order=False)
        cart_items = CartItem.objects.filter(cart=user_cart)
        context = {
            'cart': user_cart,
            'cart_items': cart_items,
        }

    except Cart.DoesNotExist:
        # Если корзины нет, создайте сообщение для отображения
        context = {
            'no_cart_message': 'Your cart is currently empty.'
        }
    return render(request, 'core/CartPage.html', context)


@login_required
@require_POST
def remove_from_cart(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk)

    # Уменьшаем количество товара в корзине на 1
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        # Если количество товара равно 1, удаляем запись о товаре из корзины
        cart_item.delete()

    # Обновляем общее количество товаров и общую стоимость корзины
    user_cart = cart_item.cart
    user_cart.total_products -= 1
    user_cart.final_price -= Decimal(cart_item.good.price)

    if user_cart.total_products == 0:
        user_cart.delete()
    else:
        user_cart.save()

    return redirect('Cart')


def add_or_remove_good(request, pk):
    minus_btn = request.POST['minus-btn']
    plus_btn = request.POST['plus-btn']
    print(f"\n\n{minus_btn}\n{plus_btn}\n\n")
    return redirect('Cart')


def reviews(request):
    pass