from .models import Blog
from django.shortcuts import redirect

def is_owner(func):
    def inner(*args, **kwargs):
        id = kwargs.get('id')
        request_user = args[0].user
        author = Blog.objects.get(id=id).author
        if request_user == author:
            return func(*args, **kwargs)
        return redirect('index')

    return inner