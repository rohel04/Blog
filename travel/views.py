from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required 
from category.models import Category
from .models import Comment
from .models import Post
from django.contrib import messages
import os
# Create your views here.
def index(request):
    top_posts=Post.objects.all().order_by('?')[:4]
    recent_post=Post.objects.filter().order_by('-id')[:3]
    post=Post.objects.all()
    tags=Category.objects.all()
    return render(request,'pages/index.html',{'post':post,'tags':tags,'recent_posts':recent_post,'top_posts':top_posts})

def about(request):
    return render(request, 'pages/about.html')


def connect(request):
    return render(request,'pages/contact.html')

def detail(request,post_id):
    post=Post.objects.filter(id=post_id)
    comments=Comment.objects.filter(post_id=post_id)
    cmt_num=comments.count()
    can_comment=False
    if not comments.filter(user_id=request.user.id):
        can_comment=True
    return render(request,'pages/post-details.html',{'post':post,'comments':comments,'cmt_num':cmt_num,'can_comment':can_comment})


def blogs(request):
    post=Post.objects.all()
    tags=Category.objects.all()
    return render(request,'pages/blog.html',{'post':post,'tags':tags})

def tags(request,cat_id):
    post=Post.objects.filter(category_id=cat_id)
    return render(request,'pages/category.html',{'post':post})


@login_required(login_url='home')
def add_blog(request):
    category=Category.objects.all()
    return render(request,'pages/add_blog.html',{'category':category})

@login_required(login_url='home')
def receive_blog(request):
    if request.method=='POST':
        cat_id=request.POST['cat_id']
        user_id=request.user.id
        title=request.POST['title']
        img=request.FILES['image']
        description=request.POST['description']

        blog=Post(
            title=title,
            category_id=cat_id,
            image=img,
            user_id=user_id,
            description=description
        )
        blog.save()
        messages.info(request,"Blog uploaded successfully")
        return render(request,'pages/add_blog.html')

@login_required(login_url='home')
def myblogs(request):
    user_id=request.user.id
    post=Post.objects.filter(user_id=user_id)
    return render(request,'pages/myblogs.html',{'post':post})
        
@login_required(login_url='home')
def edit(request,post_id):

    if request.method=='POST':
        cat_id=request.POST['cat_id']
        user_id=request.user.id
        title=request.POST['title']
        description=request.POST['description']

        blog=Post.objects.get(id=post_id)
        blog.category_id=cat_id
        blog.user_id=user_id
        blog.title=title
        blog.description=description
        if len(request.FILES):
            blog.image=request.FILES['image']
        blog.save()
        return redirect('myblogs')

        
    post=Post.objects.filter(id=post_id)
    return render(request,'pages/edit_blog.html',{'post':post})

@login_required(login_url='home')
def delete(request,post_id):
    post=Post.objects.filter(id=post_id)
    post.delete()
    return redirect('myblogs')


#for comments
@login_required(login_url='home')
def add_comment(request):
    comment=request.POST['comment']
    post_id=request.POST['post_id']
    user_id=request.user.id

    cmt=Comment(comment=comment,post_id=post_id,user_id=user_id)
    cmt.save()
    return redirect("blogs")

@login_required(login_url='home')
def delete_comment(request,cmt_id):
    comment=Comment.objects.filter(id=cmt_id)
    comment.delete()
    return redirect("blogs")