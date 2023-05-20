from django.urls import path

from market.core.views import (LoginView, UserView, CreateView, UpdatePasswordView)

urlpatterns = [
    path('create/', CreateView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='profile'),
    path('update_password/', UpdatePasswordView.as_view(), name='update_password')
]
