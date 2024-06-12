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
            const productId = item.dataset.id;
            fetch(`/product/?product_id=${productId}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    document.getElementById('modalProductImage').src = data.img_url;
                    document.getElementById('modalProductTitle').textContent = data.title;
                    document.getElementById('modalProductPrice').textContent = `${data.price} р.`;
                    document.getElementById('modalProductDescription').textContent = data.description

                    modal.classList.add('show');
                    modalContent.classList.add('show');
                })
                .catch(error => {
                    console.error('There has been a problem with your fetch operation:', error);
                });
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
