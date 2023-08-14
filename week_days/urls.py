from django.urls import path
from week_days import views as views_week_days

urlpatterns = [

    path('', views_week_days.greeting),
    path('<int:sign_number>/', views_week_days.get_week_one_number),
    path('<str:sign_week>/', views_week_days.get_week_one_days, name='week-name')
]