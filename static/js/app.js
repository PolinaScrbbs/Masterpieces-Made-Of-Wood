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


document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('productModal');
    const modalContent = modal.querySelector('.modal-content');
    const closeBtn = modal.querySelector('.close');
    const productItems = document.querySelectorAll('.products__item');

    productItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            modal.classList.add('show');
            modalContent.classList.add('show');
        });
    });

    closeBtn.addEventListener('click', () => {
        modalContent.classList.remove('show');
        modal.classList.remove('show');
    });

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modalContent.classList.remove('show');
            modal.classList.remove('show');
        }
    });
});
