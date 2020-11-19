from django.contrib import admin
from post.models import Post, PostType
# Register your models here.

admin.site.register(Post)
admin.site.register(PostType)