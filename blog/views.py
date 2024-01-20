from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post,Category
# from .models import *

# # Create your views here.
    
def home(request):
    # load all the post for db(10)
    posts= Post.objects.all()[:11]
    cats=Category.objects.all()
    data={'post':posts,'cats':cats}
    return render(request,'home.html', data)


def post(request, url):
    post= Post.objects.get(url=url)
    cats=Category.objects.all()
    # print(post)
    # data={'post':post,'cats':cats}
    return render(request, 'posts.html', {'post':post,'cats':cats})


def category(request, url):
    cat= Category.objects.get(url=url)
    posts= Post.objects.filter(cat=cat)
    data={'cat':cat,'posts':posts}
    return render(request, 'category.html', data)

def about(request):
    return render(request, 'about.html')