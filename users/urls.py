from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView,
    CustomTokenObtainPairView,
    UserDetailView,
    # UpdateUserView,
    # BlogUserAuthView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_detail'),  # Correct path
    # path('user/<int:pk>/update/', UpdateUserView.as_view(), name='user_update'),
    # path('blog/authenticate/', BlogUserAuthView.as_view(), name='blog_auth'),
]
