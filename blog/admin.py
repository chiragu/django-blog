from django.contrib import admin

# import Posts
from .models import Post

# Register your models here.


# register blog post
admin.site.register(Post)
