from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepageview),
    path('home', views.Homepageview),
    path('About', views.Aboutpageview),
    path('contact',views.Contactpageview),
    path('form', views.formpageprocess),
    path('ans', views.ansprocess),

    path('savesession', views.savesessiondata),
    path('getsession', views.getsessiondata),
    path('getsession2', views.getsesionDate2),
    path('removesession', views.delsessiondata),

    path('login', views.loginpageview, name='login'),
    path('loginprocess', views.loginprocess, name='loginprocess'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),

    path('', views.Homepageview),
    path('loginform', views.loginformview),
    path('mailsend', views.mailsendprocess),

    path('contact', views.Contactpageview),
    path('contactprocess', views.contactpageprocess),

    
]
