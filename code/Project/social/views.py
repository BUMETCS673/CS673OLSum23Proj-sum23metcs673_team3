from django.shortcuts import render, redirect
from .models import Profile, Post
from .forms import PostForm
from django.contrib.auth.models import User

# index page for social posting
def index(request):
    if not request.user.is_authenticated: # check if user already logged in
        return redirect('/') # if not, redirect to homepage

    # When user creates a post
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid(): # check if valid
            post = form.save(commit=False)
            post.user = request.user # save post's user
            post.save() # save the post
            return redirect("social") # return to the frontpage

    # show current user follows, ordered by the newest post first
    followed_posts = Post.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")

    form = PostForm(request.POST or None)
    return render(request, 'social.html', {"form": form, "posts": followed_posts})


# show all profiles of this site
def all_profile(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "all_profile.html", {"profiles": profiles})


# user's profile page
def profile(request, pk):
    if not request.user.is_authenticated: # check if user already logged in
        return redirect('/') # if not, redirect to homepage

    # handle errors
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    # get profile by user id
    profile = Profile.objects.get(pk=pk)

    # follow function - allow users to follow and unfollow others
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, "profile.html", {"profile": profile})