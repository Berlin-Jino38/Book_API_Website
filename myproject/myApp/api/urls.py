from rest_framework import routers
from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
router = routers.DefaultRouter()
router.register('author', views.AuthorAPIView, basename='author')
router.register('book', views.BookAPIView, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('auth-jwt/',TokenObtainPairView.as_view()),
    path('auth-jwt-refresh/',TokenRefreshView.as_view()),
    path('auth-jwt-verify/',TokenVerifyView.as_view()),
    
]
