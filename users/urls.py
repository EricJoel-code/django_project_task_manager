from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('logout', views.singout, name='logout'),
    path('profile/', views.profile, name='profile'),
]