from django.urls import path
from . import views

urlpatterns=[
    path('login',views.loginView,name="loginView"),
    path('register',views.registerView,name="registerView"),
    path('authenticate',views.authenticate,name="authenticate"),
    path('registration',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    
]