from django.urls import path

from django.views.generic.edit import UpdateView
from . import views

app_name = 'marche'

urlpatterns = [
    path('', views.consultationCreate, name='consultationCreate'),
    path('list/', views.consultationShow, name='consultationShow'),
    path('delete/<int:id>/', views.consultationDelete, name='consultationDelete'),
    path('<int:id>/', views.consultationEdit, name='consultationEdit'),
    path('update/<int:id>/', views.SoumissionUpdate, name='SoumissionUpdate'),

    path('soum/<int:id>/', views.SoumissionCreate, name='SoumissionCreate'),

]

