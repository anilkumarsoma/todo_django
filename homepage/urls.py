from django.conf.urls import url
from . import views

app_name = 'homepage'


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/', views.login, name="login"),
    url(r'^signup/', views.signup, name="signup"),
    url(r'^signUpUser/', views.signUpUser, name="signUpUser"),
    url(r'^loginUser/', views.loginUser, name="loginUser"),
]