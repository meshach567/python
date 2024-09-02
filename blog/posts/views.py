from django.shortcuts import render

from .models import Post

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about1(request):
    return render(request, 'about.html')

def services1(request):
    return render(request, 'services.html')

def portfolio1(request):
    return render(request, 'portfolio.html')

def team1(request):
    return render(request, 'team.html')

def blog1(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', { 'posts': posts})

def contact1(request):
    return render(request, 'contact.html')

def blogdetails1(request):
    return render(request, 'blog-details.html')

# def post(request, post_id):
#     post = Post.objects.get(pk=post_id)
#     if post is not None:
#         return render(request, 'posts/post.html', { 'post', post})
#     else:
#         raise Http404('Post does not exist')
