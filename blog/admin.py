from django.contrib import admin

from blog.models import Tag, Article


admin.site.register(Tag)
admin.site.register(Article)

