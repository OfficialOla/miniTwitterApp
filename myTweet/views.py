from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


# Create your views here.

def welcome(request):
    tweets = Post.objects.all()
    return render(request, 'myTweet/home.html', {"tweets": tweets})
    # return HttpResponse("This is my first Django code")


# def tweet_detail(request, pk):
#     try:
#         tweet = Post.objects.get(pk=pk)
#     except ObjectDoesNotExist:
#         return HttpResponse(f"Tweet {pk} does not exist")
#     return render(request, 'tweet-detail.html', {"tweet": tweet})

def tweet_detail(request, pk):
    tweet = get_object_or_404(Post, pk=pk)
    return render(request, 'myTweet/tweet-detail.html', {"tweet": tweet})


class CreatePost(generic.CreateView):
    model = Post
    template_name = 'myTweet/create-tweet.html'
    # fields = '__all__'
    fields = ['tweet', 'author']


# class Login(generic.CreateView):
#     model = Post
#     template_name = 'myTweet/templates/registration/login.html'
#     fields = ['username' 'password']
