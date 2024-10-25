from django.urls import path
from dialogue import views
urlpatterns=[
    path('chiru/<int:pid>',views.csearch),
    path('balayya/<int:pid>',views.bsearch),
    path('pk/<int:pid>',views.psearch),
]