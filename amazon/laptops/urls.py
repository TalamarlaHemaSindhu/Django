from django.urls import path
from laptops import views
urlpatterns=[
    path('hp',views.func1,name="showlaptop"),
    path('lenovo',views.func2,name="showlaptop"),
    path('dell',views.func3,name="showlaptop"),
    ]