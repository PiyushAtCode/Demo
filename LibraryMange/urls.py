from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_home, name='home'),
    path("sum/" , views.two_sum , name='two_sum')
]