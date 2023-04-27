from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="start-page"),
    path("allposts", views.allPost, name="all-posts-page"),
    path("allposts/<slug>", views.postDetail, name="post-detail-page") #/posts/my-first-post
]
