from django.shortcuts import render
from posts.models import Post

def index(request):
    first_post = Post.objects.first() 
    return render(request, 'first_post/index.html',{
        'post':first_post})
