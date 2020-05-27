from django.shortcuts import render

# import List View (for main page), Detail View (for detail pages)
from django.views.generic import ListView, DetailView

# import the models
from .models import Post

# Create your views here.

# class based view for blog post home page
class BlogListView(ListView):
    
    # set the model to Post
    model = Post

    # set the template name
    template_name = 'blog/home.html'

    # set the context object name
    context_object_name = 'post_list'


# class based view for blog post detail page
class BlogDetailView(DetailView):
    
    # set the model to Post
    model = Post

    # set the template name
    template_name = 'blog/post_detail.html'



