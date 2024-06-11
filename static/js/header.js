const burgerBtn = document.querySelector(".header__burger")
const headerBody = document.querySelector(".header__body")

burgerBtn.addEventListener("click", () => {
    headerBody.classList.toggle("hidden")
})

document.addEventListener('DOMContentLoaded', function () {
    const menuLink = document.querySelector('.header__menu');
    const dropdownMenu = document.querySelector('.dropdown-menu');

    menuLink.addEventListener('click', function (e) {
        e.preventDefault();
        dropdownMenu.classList.toggle('show');
    });
});
