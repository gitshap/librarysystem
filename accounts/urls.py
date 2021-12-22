from django.contrib.auth import login
from django.urls import path
from accounts.views import home_view, create_user, login_user, logout_user

urlpatterns = [
    path('', home_view, name='home'),
    path('employee_signup/', create_user, name='employee-signup'),
    path('login/', login_user, name='employee-login'),
    # logout url
    path('logout/', logout_user, name='logout_user')
]