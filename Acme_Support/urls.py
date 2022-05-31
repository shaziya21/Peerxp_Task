from django.urls import path
from .views import edit, dashboard, register
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView,
                                      )

app_name = 'Acme_Support'

urlpatterns = [
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='authapp/logged_out.html'), name='logout'),


]
