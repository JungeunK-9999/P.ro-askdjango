#blog-admin

from django.contrib import admin
from django.utils.safestring import mark_safe

from blog.models import Post, Comment, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'content_size', 'status',
                  'created_at', 'updated_at']

    actions=['make_draft', 'make_published']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'

    def make_draft(self, request, queryset):
        #QuerySet.update
        updated_count = queryset.update(status='d')
        # django message framework 활용
        self.message_user(request, '{}건의 포스팅을 Draft상태로 변경'.format(updated_count))
    make_draft.short_description = '  지정 포스팅을 Draft상태로 변경합니다.'

    def make_published(self, request, queryset):
        #QuerySet.update
        updated_count = queryset.update(status='p')
        # django message framework 활용
        self.message_user(request, '{}건의 포스팅을 Published상태로 변경'.format(updated_count))
    make_published.short_description = '  지정 포스팅을 Published상태로 변경합니다.'

# admin.site.register(Post, PostAdmin)    #ADMIN에 등록한 모델. 두 번하면 오류

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

    def __str__(self):
        return self.name
