from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.



horoscope_dict = {

    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'saggitarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'
}
# lst = ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']


def type(request):

    list_type = ['fire', 'earth', 'air', 'water']
    res = ''
    for i in list_type:
        result_reverse = reverse('name', args=(i, ))
        res += f"<li> <a href='{result_reverse}'> {i} </a> </li>"
    return HttpResponse(res)


def all_type_zodiac(request, sign_name):

    res = ''
    if sign_name == 'fire':
        for i in ['aries', 'leo', 'saggitarius']:
            result_reverse = reverse('horoscope-name', args=(i,))
            res += f"<li> <a href='{result_reverse}'> {i} </a> </li>"
        return HttpResponse(res)
    if sign_name == 'earth':
        for i in ['taurus', 'virgo', 'capricorn']:
            result_reverse = reverse('horoscope-name', args=(i,))
            res += f"<li> <a href='{result_reverse}'> {i} </a> </li>"
        return HttpResponse(res)
    if sign_name == 'air':
        for i in ['gemini', 'libra', 'aquarius']:
            result_reverse = reverse('horoscope-name', args=(i,))
            res += f"<li> <a href='{result_reverse}'> {i} </a> </li>"
        return HttpResponse(res)
    if sign_name == 'water':
        for i in ['cancer', 'scorpio', 'pisces']:
            result_reverse = reverse('horoscope-name', args=(i,))
            res += f"<li> <a href='{result_reverse}'> {i} </a> </li>"
        return HttpResponse(res)


def index(request):

        list_zod = list(horoscope_dict)
        data = {
            'list_zod': list_zod
        }
        return render(request, 'my_horoscope/index.html', context=data)


def get_info_zodiac_sign(request, sign_zodiac):

    list_zod_all = list(horoscope_dict)
    list_zod = horoscope_dict.get(sign_zodiac)
    data = {
        'list_zod': list_zod,
        'sign': sign_zodiac.title(),
        'list_zod_2': list_zod.split()[0],
        'list_zod_all': list_zod_all
    }
    return render(request, 'my_horoscope/info_zodiac.html', context=data)


def get_info_zodiac_number(request, sign_number):

    list_zod = list(horoscope_dict)
    if sign_number > len(list_zod):
        return HttpResponseNotFound(f'Нет такой страницы с таким знаком как {sign_number}')
    else:
        result = list_zod[sign_number - 1]
        result_reverse = reverse('horoscope-name', args=(result, ))
        return HttpResponseRedirect(result_reverse)

people = [
    {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
    {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
    {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
    {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
    {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
    {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
    {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
    {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
    {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
    {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
]
def people_task(request):

    data = {
        'people': people
    }
    return render(request, 'my_horoscope/people_task.html', context=data)


def table_heads(request):

    return render(request, 'my_horoscope/table_heads.html')







