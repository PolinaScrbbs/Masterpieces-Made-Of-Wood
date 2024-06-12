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


//========dropmenu
const service = document.querySelector(".header__openMenu");
const menu = document.querySelector(".drop-menu");

service.addEventListener("mouseenter", () => {
    menu.classList.add("show");
});

service.addEventListener("mouseleave", (event) => {
    const relatedTarget = event.relatedTarget;
    if (!menu.contains(relatedTarget)) {
        menu.classList.remove("show");
    }
});

menu.addEventListener("mouseleave", (event) => {
    const relatedTarget = event.relatedTarget;
    if (!service.contains(relatedTarget)) {
        menu.classList.remove("show");
    }
});

menu.addEventListener("mouseenter", () => {
    menu.classList.add("show");
});


//========================
document.addEventListener('DOMContentLoaded', function() {
    if (window.location.hash) {
        const hash = window.location.hash;
        history.replaceState(null, null, ' '); // убираем хеш

        setTimeout(function() {
            const element = document.querySelector(hash);
            if (element) {
                element.scrollIntoView({ behavior: 'smooth' });
            }
            history.replaceState(null, null, hash);
        }, 50);
    }
});

