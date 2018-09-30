from django.urls import path
from .import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('user_center/', views.user_center, name='user_center'),
    path('user_center_modify/', views.ModifyInfoView.as_view(), name='user_center_modify'),
    path('user_center_avatar/', views.UserImgUploadView.as_view(), name='user_center_avatar'),
    path('user_name_update/', views.UserNameUpdateView.as_view(), name='user_name_update'),
    path('user_password_update/', views.UserPasswordUpdateView.as_view(), name='user_password_update'),
]