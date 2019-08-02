import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

from dojo.forms import PostForm
from dojo.models import Post


def post_new(request):
    if request.method =='POST':
        # request.POST
        # request.FILES
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.ip=request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/list1/')
    else:
        form=PostForm()
    return render(request, 'dojo/post_form.html', {'forms':form})


def post_edit(request, id):
    post=get_object_or_404(Post, id=id)
    if request.method =='POST':
        form=PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.ip=request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/list1/')
    else:
        form=PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {'forms':form})

# Create your views here.
def mysum(request,numbers):
    result = sum(map((lambda s: int(s or 0)), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))


def post_list1(request):
    name='공유'
    return HttpResponse('''<p>여러분의 파이썬 </p>''')


def post_list2(request):
    name='공유'
    return render(request, 'dojo/post_list.html', {'name':name})


def post_list3(request):
    return JsonResponse({'message':'안녕파이썬',
                         'items':['a', 'b', 'c', 'd']},
                        json_dumps_params={'ensure_ascii': False})


def excel_download(request):
    'FBV: 엑셀 다운로드 응답하기'

    #filepath = 'C:\dev\djangoPiro\silseup\gdplev.xls'
    filepath= os.path.join(settings.BASE_DIR, 'gdplev.xls')
    filename= os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response= HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
