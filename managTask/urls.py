from django.conf.urls import url
from . import views

app_name = 'manage'


urlpatterns = [
    # /manage/
    url(r'^$', views.index, name="index"),
    # /manage/userid
    url(r'^(?P<user_id>[0-9]+)/$', views.details_user, name='details_user'),
    # Add Task
    url(r'^addTask/', views.addTask, name='addTask'),
]