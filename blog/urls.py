from django.urls import path
from django.views.decorators.cache import cache_page

from blog.views import HomeView, PostListView, PostDetailView, CreateComment

urlpatterns = [
    path('comment/<int:pk>/', CreateComment.as_view(), name='create_comment'),
    path('<slug:slug>/', PostListView.as_view(), name='post_list'),
    path('<slug:slug>/<slug:post_slug>/', PostDetailView.as_view(), name='post_single'),
    path('', cache_page(60 * 15)(HomeView.as_view()), name='home'),
]
