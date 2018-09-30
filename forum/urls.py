from django.urls import path, include
from .import views

app_name = 'forum'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.TopicDetailView.as_view(), name='detail'),
    path('pub/<str:username>/topic/<int:pk>/', views.pub_topic, name='pub'),
    path('pub/<str:username>/commit/<int:board_id>/', views.commit_topic, name='pub_commit'),
    path('boards/', views.BoardsView.as_view(), name='boards'),
    path('board_detail/<int:pk>/', views.BoardDetailView.as_view(), name='board_detail'),
    path('topic_delete/<int:pk>/', views.topic_delete, name='topic_delete'),
    path('topic_update/<int:pk>/', views.TopicUpdateView.as_view(), name='topic_update'),
    path('tag_detail/<int:pk>/', views.TagsView.as_view(), name='tag_detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # 富文本编辑前端url
    path('user_topics/<int:pk>/', views.UserTopicsView.as_view(), name='user_topics'),
]