from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('subjects/', views.subjects, name='subjects'),
    path('grades/', views.grades, name='grades'),
    path('report/', views.report, name='report'),
]
