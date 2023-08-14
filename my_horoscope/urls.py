from django.urls import path
from my_horoscope import views as views_horoscope

urlpatterns = [

    path('', views_horoscope.index, name='index-name'),
    path('type/', views_horoscope.type),
    path('people/', views_horoscope.people_task),
    path('people/table/', views_horoscope.table_heads),
    path('<int:sign_number>/', views_horoscope.get_info_zodiac_number),
    path('type/<str:sign_name>/', views_horoscope.all_type_zodiac, name='name'),
    path('<str:sign_zodiac>/', views_horoscope.get_info_zodiac_sign, name='horoscope-name')
]