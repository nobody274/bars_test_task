from django.urls import path

from . import views

app_name = 'sith_recruiting'
urlpatterns = [
    path('', views.index, name='index'),
    path('recruit/', views.recruit, name='recruit'),
    path('sith/', views.sith, name='sith'),
    path('recruit/trial/<int:new_recruit_id>/', views.recruit_trial, name='trial'),
]