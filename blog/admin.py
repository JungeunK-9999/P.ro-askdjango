#blog-admin

from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'created_at', 'updated_at']

# admin.site.register(Post, PostAdmin)    #ADMIN에 등록한 모델. 두 번하면 오류
