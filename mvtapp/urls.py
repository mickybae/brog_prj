from django.urls import path
#from django.views import detail
from mvtapp.views import detail

app_name = 'mvtapp'

urlpatterns = (
    path('detail/', detail, name='detail'),
)