from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import  datetime
from django.shortcuts import redirect
# Create your views here.


def homepage(request):
    posts = Post.objects.all()  #获取所有的数据项
    now = datetime.now()
    context = {'posts': posts, 'now': now}
    return render(request, 'index.html', context)  #返回给index.html文件


def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        context = {'post': post}
        if post != "None":
            return render(request, 'post.html', context)
    except:
        return redirect('/')


