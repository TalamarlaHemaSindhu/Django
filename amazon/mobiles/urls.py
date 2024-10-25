from django.urls import path
from mobiles import views
urlpatterns=[
    path('samsung',views.func1,name="showmobile"),
    path('vivo',views.func2,name="showmobile"),
    path('realme',views.func3,name="showmobile"),]