from django.contrib import admin

from blog.models import Post,Lesson,Profile

# Register your models here.

admin.site.register(Post)
admin.site.register(Lesson)
admin.site.register(Profile)
