from django import forms
from django.forms import ModelForm
from blog.models import Tag, Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'tags']
