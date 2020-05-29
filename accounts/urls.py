# import path
from django.urls import path

# import SignUpView
from .views import SignUpView


# url patterns
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]