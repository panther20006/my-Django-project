from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepageview),
    path('home', views.Homepageview),
    path('About', views.Aboutpageview),
    path('contact',views.Contactpageview),
    path('form', views.formpageprocess),
    path('ans', views.ansprocess),
    path('form', views.formpageprocess, name='form'),
    path('ans', views.ansprocess, name='ans'),

    path('savesession', views.savesessiondata),
    path('getsession', views.getsessiondata),
    path('getsession2', views.getsesionDate2),
    path('removesession', views.delsessiondata),

    path('login', views.loginpageview),
    path('loginprocess', views.loginprocess),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    
]
