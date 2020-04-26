from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView, UserPostListView

urlpatterns = [
    # path('post/<int:pk>/comment/', AddComment.as_view(), name='add-comment'),
    path('', PostListView.as_view(), name= 'blog-home' ),
    path('post/<int:pk>/',  PostDetailView.as_view(), name= 'post-detail' ),
    path('user/<str:username>', UserPostListView.as_view(), name= 'user-posts'),
    path('post/<int:pk>/update/',  PostUpdateView.as_view(), name= 'post-update' ),
    path('post/<int:pk>/delete/',  PostDeleteView.as_view(), name= 'post-delete' ),
    path('post/new/',  PostCreateView.as_view(), name= 'post-create' ),
    path('post/<int:pk>/comment/', views.add_comment, name='add-comment'),
    path('about/', views.about, name='blog-about'),
]
