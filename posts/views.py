from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post


def archive(request):
    posts = Post.objects.all()
    return render(request, 'posts/archive.html', {
        'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {
        'post':post})
