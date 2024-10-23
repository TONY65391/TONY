from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('js1/', views.jss1, name = 'js1'),
    path('js1/djs1/<int:id>', views.djss1, name = 'djs1'),
    path('js2/', views.jss2, name = 'js2'),
    path('js2/djs2/<int:id>', views.djss2, name = 'djs2'),
    path('js3/', views.djss3, name = 'djss3'),
    path('js3/djs3/<int:id>', views.djss3, name = 'djss3' )
]