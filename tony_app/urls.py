from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('js1/', views.jss1, name = 'js1'),
    path('js1/djs1/<int:id>', views.djss1, name = 'djs1')
]