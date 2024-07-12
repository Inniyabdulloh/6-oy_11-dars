from django.shortcuts import render, redirect
from . import models


def blogs(request):
    posts = models.Blog.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'blogs.html', context)


def blog_detail(request, id):
    blog = models.Blog.objects.get(id=id)
    socials = models.SocialMedia.objects.filter(user=blog.author)
    comments = models.Comment.objects.filter(blog=blog)
    context = {
        'blog':blog,
        'socials':socials,
        'comment_count':comments.count(),
        'comments':comments
    }
    return render(request, 'blog-detail.html', context)


def comment_create(request):
    message = request.POST['message']
    blog_id = request.POST['blog_id']
    models.Comment.objects.create(
        author=request.user,
        body=message,
        blog_id=blog_id
    )
    return redirect('blog_detail', blog_id)

