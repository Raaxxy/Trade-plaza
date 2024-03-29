from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('policy/',views.policy,name='policy'),
    path('license/',views.license,name='license'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',views.logout_view, name='logout'),
] 
