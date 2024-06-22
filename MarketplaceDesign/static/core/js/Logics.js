function toggleMenu() {
    let subMenu = document.getElementById("SearchMenu");
    subMenu.classList.toggle("open_menu");

    // Сохраняем состояние меню в localStorage
    if (subMenu.classList.contains("open_menu")) {
        localStorage.setItem("menuOpen", "true");
    } else {
        localStorage.setItem("menuOpen", "false");
    }
}

// Проверяем состояние меню при загрузке страницы
window.addEventListener("load", function () {
    let subMenu = document.getElementById("SearchMenu");
    if (localStorage.getItem("menuOpen") === "true") {
        subMenu.classList.add("open_menu");
    }
});


// Amount of goods

function increase(input_id) {
    var input = document.getElementById(input_id);
    var value = parseInt(input.value);
    input.value = value + 1;
}

function decrease(input_id) {
    var input = document.getElementById(input_id);
    var value = parseInt(input.value);
    if (value > 0) {
    input.value = value - 1;
    }
}





// $(document).ready(function() {
//     $('#search-input').on('input', function() {
//         var query = $(this).val();
//         if (query) {
//             $.ajax({
//                 type: 'GET',
//                 url: '/search/',
//                 data: { query: query },
//                 success: function(data) {
//                     $('#search-results').html(data);
//                 }
//             });
//         } else {
//             // Если поле ввода пустое, очистите результаты поиска.
//             $('#search-results').empty();
//         }
//     });
// });
