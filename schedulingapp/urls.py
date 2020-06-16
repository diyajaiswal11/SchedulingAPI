
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.home,name='home'), #makes call to API
    path('ping/',views.ping,name='ping'), #sends GET request to /ping endpoint
    path('test/<str:url>/<str:date>/',views.test,name='test'), #API call having two parameters, url and date-time
    path('<str:url>/',views.test1,name='test1'), #GET request to url specified
]
