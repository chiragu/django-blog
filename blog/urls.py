# import path
from django.urls import path

# import BlogListView

from .views import BlogListView, BlogDetailView

# url patterns
urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]