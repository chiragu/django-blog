from django.shortcuts import render

# import List View (for main page), Detail View (for detail pages), CreateView for new post form,
# UpdateView for editing post, deleteview for deletion
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView,
 )

# import the models
from .models import Post

# import reverse lazy (waits for redirect until post deleted as opposed to reverse)
from django.urls import reverse_lazy

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

# class based view for new blog post form page (login required)

class BlogCreateView(CreateView):
    
    # set the model to Post
    model = Post

    # set the template name
    template_name = 'blog/post_new.html'

    # set the fields of the form
    fields = ['title', 'author', 'body']

# class based view for update blog post form page
class BlogUpdateView(UpdateView):
    
    # set the model to Post
    model = Post

    # set the template name
    template_name = 'blog/post_edit.html'

    # update the fields of the form
    fields = ['title', 'body']

# class based view for delete blog post confirmation page
class BlogDeleteView(DeleteView):
    
    # set the model to Post
    model = Post

    # set the template name
    template_name = 'blog/post_delete.html'

    # on success, redirect home
    success_url = reverse_lazy('home')



