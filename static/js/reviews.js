const modal = document.getElementById("myModal");
const btn = document.getElementById("openFeedbackBtn");
const span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.classList.add("show");
}

span.onclick = function() {
    modal.classList.remove("show");
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.classList.remove("show");
    }
}
//=========кастом dropdown

$('.dropdown').click(function () {
    $(this).attr('tabindex', 1).focus();
    $(this).toggleClass('active');
    $(this).find('.dropdown-menu').slideToggle(300);
});
$('.dropdown').focusout(function () {
    $(this).removeClass('active');
    $(this).find('.dropdown-menu').slideUp(300);
});
$('.dropdown .dropdown-menu li').click(function () {
    $(this).parents('.dropdown').find('span').text($(this).text());
    $(this).parents('.dropdown').find('input').attr('value', $(this).attr('id'));
});
/*End Dropdown Menu*/


$('.dropdown-menu li').click(function () {
var input = '<strong>' + $(this).parents('.dropdown').find('input').val() + '</strong>',
  msg = '<span class="msg">Hidden input value: ';
$('.msg').html(msg + input + '</span>');
});

//=======оценки
function updateFeedbackText() {
    const feedbackText = {
        5: 'Отлично!',
        4: 'Хорошо!',
        3: 'Неплохо.',
        2: 'Плохо.',
        1: 'Ужасно!'
    };

    const selectedRating = document.querySelector('input[name="star"]:checked');
    const feedbackEstElement = document.querySelector('.feedback-est');

    if (selectedRating) {
        feedbackEstElement.textContent = feedbackText[selectedRating.value];
    } else {
        feedbackEstElement.textContent = '';
    }
}

//=-================
document.addEventListener('DOMContentLoaded', function () {
    var select = document.querySelector('.dropdown .select');
    var menu = document.querySelector('.dropdown-menu');
    var hiddenInput = document.querySelector('input[name="product"]');

    select.addEventListener('click', function () {
        menu.classList.toggle('show');
    });

    menu.addEventListener('click', function (e) {
        var target = e.target;
        if (target.tagName === 'LI') {
            hiddenInput.value = target.getAttribute('data-value');
            select.querySelector('span').textContent = target.textContent;
            menu.classList.remove('show');
        }
    });
});

//================
document.querySelectorAll('.dropdown-menu li').forEach(function(item) {
    item.addEventListener('click', function() {
        var value = this.getAttribute('data-value');
        document.getElementById('product-id').value = value;
    });
});

//===================Префикc @
document.addEventListener("DOMContentLoaded", function() {
    const input = document.getElementById('input-email');
    const prefix = '@';
    let prefixAdded = false;

    input.addEventListener('input', function(event) {
        if (!prefixAdded && input.value.length > 0) {
            input.value = prefix + input.value;
            prefixAdded = true;
        } else if (input.value === '') {
            prefixAdded = false;
        }
    });

    input.addEventListener('keydown', function(event) {
        if (prefixAdded && input.selectionStart <= prefix.length && (event.key === 'Backspace' || event.key === 'Delete')) {
            event.preventDefault();
        }
    });

    input.addEventListener('paste', function(event) {
        event.preventDefault();
        const paste = (event.clipboardData || window.clipboardData).getData('text');
        const selectionStart = input.selectionStart;
        const selectionEnd = input.selectionEnd;

        if (prefixAdded) {
            if (selectionStart < prefix.length) {
                input.value = prefix + paste + input.value.substring(selectionEnd);
            } else {
                input.value = input.value.substring(0, selectionStart) + paste + input.value.substring(selectionEnd);
            }
        } else {
            input.value = paste;
            if (input.value.length > 0) {
                input.value = prefix + input.value;
                prefixAdded = true;
            }
        }
    });
});