from django.conf.urls import url
from . import views

app_name = 'trader'
urlpatterns = [
    urll(r'^$', views.index, name='index'),
]