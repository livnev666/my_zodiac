from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

week_dict = {

    'sunday': 'В гости ходит ВОСКРЕСЕНЬЕ, Очень любит угощение. '
              'Это самый младший брат, К Вам зайти он будет рад.',
    'monday': 'Старший братец ПОНЕДЕЛЬНИК — Работяга, не бездельник. '
              'Он неделю открывает Всех трудиться заставляет.',
    'tuesday': 'ВТОРНИК следует за братом У него идей богато, '
               'Он за все берется смело И работа закипела.',
    'wednesday': 'Вот и средняя сестрица Не пристало ей лениться, '
                 'А зовут её СРЕДА, Мастерица хоть куд',
    'thursday': 'Брат ЧЕТВЕРГ и так и сяк, Он мечтательный чудак '
                'Повернул к концу недели И тянулся еле еле.',
    'friday': 'ПЯТНИЦА — сестра сумела Побыстрей закончить закончить дело. '
              'Если делаешь успехи, Время есть и для потехи.',
    'saturday': 'Предпоследний брат СУББОТА Не выходит на работу. '
                'Шалопай и озорник Он работать не привык.'

}

def greeting(request):

    return render(request, 'week_days/greeting.html')


def get_week_one_days(request, sign_week):

    list_week = list(week_dict)
    if sign_week not in list_week:
        return HttpResponseNotFound('Нет такой страницы')
    else:
        dc = week_dict.get(sign_week)
        return HttpResponse(dc)


def get_week_one_number(request, sign_number):

    list_week = list(week_dict)
    if sign_number > len(list_week):
        return HttpResponseNotFound(f'Нет такой страницы с днем {sign_number}')
    else:
        result = list_week[sign_number - 1]
        rever_url = reverse('week-name', args=(result, ))
        return HttpResponseRedirect(rever_url)