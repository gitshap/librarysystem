from django.contrib.auth import login
from django.urls import path
from accounts.views import home_view, create_user, login_user

urlpatterns = [
    path('', home_view, name='home'),
    path('employee_signup/', create_user, name='employee-signup'),
    path('login/', login_user, name='employee-login'),
]