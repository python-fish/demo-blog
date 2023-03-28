from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views import View
from django.urls import reverse

from blog.models import Article, Tag
from blog.forms import ArticleForm


# 主页：列表页
class IndexView(View):
    def get(self, request):
        articles = Article.objects.all()
        context = {
            'article_list': articles,
        }
        return render(request, 'blog/index.html', context)

# def index(request):
#     articles = Article.objects.all()
#     template = loader.get_template('blog/index.html')
#     context = {
#         'article_list': articles,
#     }
#     return render(request, 'blog/index.html', context)
    # return HttpResponse(template.render(context, request))
    # output = ','.join([article.title for article in articles])
    # return HttpResponse(output)


# 详情页
class DetailView(View):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        article = get_object_or_404(Article, pk=kwargs.get('article_id'))
        context = {
            'article': article
        }
        return render(request, 'blog/detail.html', context)

# def detail(request, article_id):
#     article = get_object_or_404(Article, pk=article_id)
#     # try:
#     #     article = Article.objects.get(pk=article_id)
#     # except Article.DoesNotExist:
#     #     raise Http404("Article does not exist")
#     context = {
#         'article': article
#     }
#     return render(request, 'blog/detail.html', context)
    # return HttpResponse(f"你正在查看ID为{article_id}文章的详情")

# 创建文章
class ArticleCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        context = {
            'form': form
        }
        return render(request, 'blog/create.html', context)

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()
            return redirect('/blog/')


# 编辑文章
class ArticleEditView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get("article_id"))
        form = ArticleForm(instance=article)
        context = {
            'form': form
        }
        return render(request, 'blog/edit.html', context)
    
    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get("article_id"))
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()
            return redirect(reverse('article-detail', kwargs={'article_id': kwargs.get("article_id")}))
        else:
            context = {
                'form': form
            }
            return render(request, 'blog/edit.html', context)


class ArticleDeleteView(View):
    def delete(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get("article_id"))
        article.delete()
        return HttpResponse('')

# def create(request):
#     if request.method == 'POST':
#         print(request.POST)
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             article = form.save(commit=False)
#             article.author = request.user
#             article.save()
#             form.save_m2m()
#             return redirect('/blog/')
#     else:
#         form = ArticleForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'blog/create.html', context)