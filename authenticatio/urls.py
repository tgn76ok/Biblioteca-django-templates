from django.urls import path
from .views import index

app_name='authenticatio'

urlpatterns = [
    path('',index,name='index' ),
]