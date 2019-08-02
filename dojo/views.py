import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from dojo.forms import PostForm
from dojo.models import Post


def post_new(request):
    if request.method =='POST':
        # request.POST
        # request.FILES
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            # # 방법1
            # print(form.cleaned_data)
            # post=Post()
            # post.title=form.cleaned_data['title']
            # post.content=form.cleaned_data['content']
            # post.save()
            #
            # # 방법2
            # post=Post(title=form.cleaned_data['title'],
            #           content=form.cleaned_data['content'])
            # post.save()
            #
            # # 방법3
            # post=Post.objects.create(title=form.cleaned_data['title'],
            #                          content=form.cleaned_data['content'])
            # post.save()

            # 방법4
            post=Post.objects.create(**form.cleaned_data)

            return redirect('/dojo/list1/')
    else:
        form=PostForm()
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
