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

