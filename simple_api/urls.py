from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views.auth_views import register_user,login_user
from .views.main_views import category_view,categoryby_id,product_view,productby_id,category_products,category_with_products
urlpatterns = [
    path('register/',register_user),
    path('login/',login_user),
    path('token/refresh',TokenRefreshView.as_view()),
    path('category/',category_view),
    path('category/<int:id>',categoryby_id),
    path('product/',product_view),
    path('product/<int:id>',productby_id),
    path('categoryby_id/<int:category_id>',category_products),
    path('category_products/',category_with_products)
]
