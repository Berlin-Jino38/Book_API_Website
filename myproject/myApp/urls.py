from . import views
from django.urls import path

urlpatterns = [
    path('',views.Auther_view,name='index'),
    path('<str:name>/',views.Book_view,name='book'),
    path('search',views.search_view,name='search'),
    path('signup',views.signup,name='signup'),
]