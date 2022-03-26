from django.urls import path
from .views import index,image_location, search_results



urlpatterns = [
    path('',index,name='index')
]