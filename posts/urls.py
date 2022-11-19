from django.urls import path
from .views import (
    PostListView, 
    PostCreateView, 
    PostDetailView
)

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('new/', PostCreateView.as_view(), name='new'),
]