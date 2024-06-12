document.addEventListener("DOMContentLoaded", function() {
    const button = document.querySelector(".intro__btn");
    const servicesSection = document.querySelector(".services");

    button.addEventListener("click", function() {
        const offset = 100;
        const elementPosition = servicesSection.getBoundingClientRect().top + window.pageYOffset;
        const offsetPosition = elementPosition - offset;

        window.scrollTo({
            top: offsetPosition,
            behavior: "smooth"
        });
    });
});
