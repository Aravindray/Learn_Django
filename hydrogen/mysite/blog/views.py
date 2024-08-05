from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from .forms import PostShareForm
from django.core.mail import send_mail

def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    return render(request, 'blog/post/list.html', {'posts':posts})

def post_detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post,
                           publish__year=year,
                           publish__month=month,
                           publish__day=day,
                           slug=post_slug,
                           status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post':post})

def post_share(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = PostShareForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommend you '{post.title}'"
            message = f"Read this post {post_url}\n\n"\
                      f"commends: {cd['comment']}"
            sender = cd['send']
            send_mail(subject, message, sender, [cd['to']], fail_silently=False)
            sent = True
    else:
        form = PostShareForm()
    
    return render(request, 'blog/post/share.html', {'post':post,
                                                    'form':form,
                                                    'sent':sent})
