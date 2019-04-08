from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('spiderman',views.spiderman,name='spiderman'),
    path('tony',views.ironmman),
    path('antman',views.antman),
    path('antman/',views.endingtrail),
    path('<int:question_id>/results',views.results,name='results'),
    path('<int:question_id>',views.detail,name='question'),
    path('<int:question_id>/vote',views.vote,name='vote'),
]