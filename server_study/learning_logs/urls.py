"""define URL pattern of learning_logs"""

from django.urls import path, include, re_path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # homepage
    path("",views.index,name='homepage'),
    path("topics/",views.topics,name='topics'),
    re_path("topics/(?P<topic_id>\d+)/",views.topic,name='topic'),
    path("new_topic/",views.new_topic,name='new_topic'),
    re_path("new_entry/(?P<topic_id>\d+)/",views.new_entry,name='new_entry'),
    re_path("edit_entry/(?P<entry_id>\d+)",views.edit_entry,name='edit_entry'),
]