from django.urls import path
from .views import sign_in, register, logout_user, result, ajax_reg, ajax_log_passwd

urlpatterns = [
    path('login', sign_in, name='login'),
    path('register', register, name='register'),
    path('logout', logout_user, name='logout'),
    path('result', result, name='result'),
    path('ajax_reg', ajax_reg, name='ajax_reg'),
    path('ajax_log_passwd', ajax_log_passwd, name='ajax_log_passwd'),
]
