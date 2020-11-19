from django.shortcuts import render, redirect
from post.models import Post
from post.forms import AddBoastOrRoast

# Create your views here.


def index_view(request):
    posts = Post.objects.all().order_by("created_at")[::-1]
    return render(request, "index.html", {'posts': posts})


def add_boast_or_roast(request):
    if request.method == 'POST':
        form = AddBoastOrRoast(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                is_boast=data['is_boast'],
                text=data['text'],
            )
            return redirect('/')
    form = AddBoastOrRoast()
    return render(request, 'add_form.html', {'form': form})


def like_view(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    post.likes += 1
    post.vote_score += 1
    post.save()
    return redirect('/')


def dislike_view(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    post.dislikes += 1
    post.vote_score -= 1
    post.save()
    return redirect('/')


def roast_view(request):
    posts = Post.objects.all().filter(is_boast_id=2)[::-1]
    return render(request, 'roast.html', {'posts': posts})


def boast_view(request):
    posts = Post.objects.all().filter(is_boast_id=1)[::-1]
    return render(request, 'boast.html', {'posts': posts})


def vote_score_view(request):
    posts = Post.objects.all().order_by('-vote_score')
    return render(request, 'sort_by_vote.html', {'posts': posts})
