"""define URL pattern of learning_logs"""

from django.urls import path, include

from . import views


urlpatterns = [
    # homepage
    path("",views.index,name='index')
]