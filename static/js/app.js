document.addEventListener("DOMContentLoaded", function() {
    const showMoreBtn = document.getElementById('showMoreBtn');
    const showLessBtn = document.getElementById('showLessBtn');
    const productsItems = document.querySelectorAll('.products__item');

    showMoreBtn.addEventListener('click', function() {
        productsItems.forEach((item, index) => {
            if (index >= 4) {
                item.style.display = 'block';
            }
        });
        showMoreBtn.style.display = 'none';
        showLessBtn.style.display = 'block';
    });

    showLessBtn.addEventListener('click', function() {
        productsItems.forEach((item, index) => {
            if (index >= 4) {
                item.style.display = 'none';
            }
        });
        showMoreBtn.style.display = 'block';
        showLessBtn.style.display = 'none';
    });
});
