from django.urls import path
from .views import (
    UserRegistrationView, UserLoginView,
    ProductListCreateView, PurchaseCreateView, ProductListView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    # User registration URL
    path('register/', UserRegistrationView.as_view(), name='user-registration'),

    # User Login URL
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Products URL
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('purchase/', PurchaseCreateView.as_view(), name='purchase-create'),
    path('products-list/', ProductListView.as_view(), name='product-list'),
]