from django import template
from datetime import datetime
import pytz

register = template.Library()

@register.filter
def times(number):
    return range(int(number))

MONTH_NAMES = {
    "January": "января",
    "February": "февраля",
    "March": "марта",
    "April": "апреля",
    "May": "мая",
    "June": "июня",
    "July": "июля",
    "August": "августа",
    "September": "сентября",
    "October": "октября",
    "November": "ноября",
    "December": "декабря",
}

@register.filter
def date_format(date_obj):
    if isinstance(date_obj, datetime):
        tz_moscow = pytz.timezone('Europe/Moscow')
        date_obj = date_obj.astimezone(tz_moscow)
        
        month_name_ru = MONTH_NAMES.get(date_obj.strftime("%B"))
        
        date_str = date_obj.strftime("%d %B %Y года, %H:%M").replace(date_obj.strftime("%B"), month_name_ru)
        return date_str
    else:
        return date_obj
    
@register.filter
def feedback_message(estimation):
    if estimation == 5:
        return "Отлично!"
    elif estimation == 4:
        return "Хорошо!"
    elif estimation == 3:
        return "Неплохо."
    elif estimation == 2:
        return "Плохо."
    elif estimation == 1:
        return "Ужасно!"
    else:
        return "Без оценки"