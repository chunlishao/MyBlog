from datetime import date
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

all_posts = [
    {
        "slug": "hike in the mountain",
        "image": "mountains.jpg",
        "author": "chunli",
        "date": date(2023, 4, 27), 
        "excerpt": "this is the excerpt",
        "content": "this is dummy content. "
    },
    
    {
        "slug": "coding is fun",
        "image": "coding.jpg",
        "author": "chunli",
        "date": date(2023, 3, 27), 
        "excerpt": "this is the excerpt",
        "content": "this is dummy content. "
    },
    
    {
        "slug": "wood",
        "image": "woods.jpg",
        "author": "chunli",
        "date": date(2023, 2, 27), 
        "excerpt": "this is the excerpt",
        "content": "this is dummy content. about wood "
    }
]

def get_key(post):
    return post['date']
    

def index(request):
    latest_posts = sorted(all_posts, key= get_key)[-3:]
    
    return render(request, "welcome.html", {
        "latest_posts" : latest_posts
    })

def allPost(request):
    try:
        return render(request, "all-posts.html", {
            "all_posts" : all_posts
        })
    except:
        raise Http404()
    
def postDetail(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "post-detail.html", {
        "post":post
    })
