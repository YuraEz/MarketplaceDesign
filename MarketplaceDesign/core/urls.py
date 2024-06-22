from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name='Main'),
    path("catalog", views.catalog, name='Catalog'),
    path("good-info/<int:pk>/", views.good_info, name='GoodInfo'),

    path("add-in-cart/<int:pk>/", views.add_in_cart, name='AddInCart'),
    path("cart", views.cart, name='Cart'),
    path("remove-from-cart/<int:pk>/", views.remove_from_cart, name='RemoveFromCart'),
    path("add-or-remove/<int:pk>/", views.add_or_remove_good, name='AddOrRemove'),

    path('reviews/', views.reviews, name='reviews'),

    path('get', views.search_view, name='search'),
]
