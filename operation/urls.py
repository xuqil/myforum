from django.urls import path
from .import views

app_name = 'operation'

urlpatterns = [
        path('comment/<int:pk>/', views.comment, name='comment'),
        path('add_fav/<int:pk>/', views.favorite_topics, name='add_fav'),
        path('comment/', views.user_comment, name='user_comment'),
]