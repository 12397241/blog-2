from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {"posts": posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {"post", post})


# Create your views here.
def index(request):
    return HttpResponse('<h1>My first http response</h1>')


def hello(request):
    return HttpResponse("Hello<br>World!!!")
