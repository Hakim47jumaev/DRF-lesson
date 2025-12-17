from .views import *
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('register/',Register.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('login/refresh',TokenRefreshView.as_view()),
    path('logout/',Logout.as_view()),
]
