from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views.auth_views import register_user,login_user
urlpatterns = [
    path('register/',register_user),
    path('login/',login_user),
    path('token/refresh',TokenRefreshView.as_view())
]
