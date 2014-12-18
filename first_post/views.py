from django.shortcuts import render
from posts.models import Post

def index(request):
    #'last' because posts ordering by created on
    first_post = Post.objects.last() 
    return render(request, 'first_post/index.html',{
        'post':first_post})
