from django.conf.urls import url
from . import views

app_name = 'trader'
urlpatterns = [
    url(r'discretebar/', discretebarview.index, name='index'),
    url(r'piechart/', piechartview.index2, name='index2'),
]


"""

from django.conf.urls import url
from . import views

app_name = 'trader'
urlpatterns = [
    url(r'discretebar/', discretebarview.index, name='index'),
    url(r'piechart/', piechartview.index_2, name='index_2'),
]

"""
