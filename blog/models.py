from django.db import models

# Create your models here.

# model for a blog post
class Post(models.Model):

    # title field with a max length of 200 chars
    title = models.CharField(max_length=200)

    # auto field that is many to one.. (many posts can have same author but one post cannot have multiple authors)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    # body of the post is a text field
    body = models.TextField()


    # to string for admin interface/tests
    def __str__(self):
        return self.title