from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import PostForm
from blog.models import Post


def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'q': q,
    })


def post_detail(request, id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404

    post = get_object_or_404(Post, id=id)

    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)   #get_absoulute_url
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })

def post_edit(request, id):
    post=get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post)   #get_absoulute_url
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
    })