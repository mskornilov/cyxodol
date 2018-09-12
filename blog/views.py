from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from common.decorators import ajax_required
from django.http import JsonResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm, LikeForm
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})

@login_required
def post_detail(request, post_id):
    if request.method == 'POST':
        likeForm = LikeForm(data=request.POST)
        form = CommentForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            comment = Comment.objects.create(post_id=post_id)
            comment.author=cd['author']
            comment.text=cd['text']
            comment.save()
        if likeForm.is_valid():
            cdLike = likeForm.cleaned_data
            post_liked = Post.objects.get(id=post_id)
            post_liked.likes += 1
            post_liked.save()
    post = Post.objects.get(id=post_id)
    comments = post.comments.all()
    form = CommentForm()
    likeForm = LikeForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form,
                                                    'comments': comments,
                                                    'likeform': likeForm})

def post_update(request, post_id):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        post = Post.objects.get(id=post_id)
        if form.is_valid():
            cd = form.cleaned_data
            post.text = cd['text']
            post.name = cd['name']
            post.save()
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)
    return render(request, 'blog/post_update.html', {'form': form, 'post': post})

@login_required
@ajax_required
def post_like(request):
    post_id = request.POST.get('id')
    if post_id:
        try:
            post = Post.objects.get(id=post_id)
            post.likes += 1
            post.save()
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})
# добавить предыдущее действие, нельзя было лайкнуть много раз
