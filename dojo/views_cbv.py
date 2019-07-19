from django.http import HttpResponse
from django.views.generic import View, TemplateView


class PostList1(View):
    def get(self, request):
        # name='공유'
        html= self.get_temlate_string()
        return HttpResponse(html)

    def get_temlate_string(self):
        return '''<h1>여러분의 친구인 파이썬입니다.</h1>
        <h2>헉 됐어...!!</h2>'''
post_list1=PostList1.as_view()

class PostList2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context=super().get_context_data()
        context['name']='공유'
        return context
post_list2=PostList2.as_view()



class PostList3(View):
    pass


class ExcelDownload(View):
    pass