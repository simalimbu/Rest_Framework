from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views.auth_views import register_user,login_user
from .views.main_views import category_view,categoryby_id
urlpatterns = [
    path('register/',register_user),
    path('login/',login_user),
    path('token/refresh',TokenRefreshView.as_view()),
    path('category/',category_view),
    path('category/<int:id>',categoryby_id)
]
