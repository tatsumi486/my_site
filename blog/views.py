from datetime import date 
from django.shortcuts import render, get_object_or_404

from .models import BlogPost, Author, Tag

# Create your views here.
def index(request):
    latest_posts = BlogPost.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts":latest_posts})

def posts(request):
    all_posts = BlogPost.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"posts": all_posts})

def post_details(request, slug):
    id_post = BlogPost.objects.get(slug=slug)
    return render(request, "blog/post-detail.html", {"post":id_post, "post_tags": id_post.tags.all()})