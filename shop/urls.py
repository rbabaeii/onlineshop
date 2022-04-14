from django.urls import path , include
from .views import Foods , Neworder
urlpatterns = [
    path('foods/' , Foods.as_view()) , 
    path('newOrder' , Neworder.as_view())
]