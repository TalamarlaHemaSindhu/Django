from django.urls import path
from app1 import views
urlpatterns=[
    path('',views.home,name="homepage"),
    path('login',views.loginView,name="loginpage"),
    path('profile',views.profile,name="profilepage"),
    path('register',views.register,name="registerpage"),
    path('create',views.create,name="createpage"),
    path('delete',views.deleteView,name="deletepage"),
    path('logout',views.logoutView,name="logoutpage"),
    
    
    
]