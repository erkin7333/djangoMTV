from django.urls import path
from .views import (LandingPageView, customuser_list, customuser_detail, user_create, user_update, user_delete,
                    UserListView, UserCreateView, UserDeatailView, UserUpdateView)
from .registerviews import UserRegisterView, user_login, user_logout
from .signupview import SignupView


app_name = "user"

urlpatterns = [
    path('', LandingPageView.as_view(), name='home'),
    path('user/list/', UserListView.as_view(), name='customuser_list'),
    path('user_detail/<int:pk>/', UserDeatailView.as_view(), name='user_detail'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),
    path('user_update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user_delete/<int:id>/', user_delete, name='user_delete'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', SignupView.as_view(), name='signup')
]