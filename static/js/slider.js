var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1.5,
    spaceBetween: 0,
    centeredSlides: false,
    loop: true,
    slidesOffsetBefore: 265,
    autoplay: {
        delay: 5000,
    },
    initialSlide: 3,

    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },

    breakpoints: {
        // когда ширина экрана меньше или равна 768px
        1024: {
            slidesPerView: 1.5,
            spaceBetween: 0,
            slidesOffsetBefore: 265,
        },
        992: {
            slidesPerView: 1.5,
            spaceBetween: 0,
            slidesOffsetBefore: 265,
        },
        768: {
            slidesPerView: 1,
            spaceBetween: 40,
            slidesOffsetBefore: 0,
        },
        // для больших экранов оставляем значения по умолчанию
        425: {
            slidesPerView: 1,
            spaceBetween: 220,
            slidesOffsetBefore: 0,
        },
        322: {
            slidesPerView: 1,
            spaceBetween: 20,
            slidesOffsetBefore: 0,
        },
    }
  
});
