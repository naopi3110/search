from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.form, name='form'),
    path('1', views.form1, name='form1'),
    path('2', views.form2, name='form2'),
    path('3', views.form3, name='form3'),
    path('4', views.form4, name='form4'),
    path('5', views.form5, name='form5'),
    path('6', views.form6, name='form6'),
    path('7', views.form7, name='form7'),
    path('form/', views.index, name='index'),
    path('form1/', views.index1, name='index1'),
    path('form2/', views.index2, name='index2'),
    path('form3/', views.index3, name='index3'),
    path('form4/', views.index4, name='index4'),
    path('form5/', views.index5, name='index5'),
    path('form6/', views.index6, name='index6'),
    path('form7/', views.index7, name='index7'),
]##ここは適宜追加する都度uploadします。