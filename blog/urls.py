from django.urls import path

from blog import views
from blog.views import (
    IndexView, DetailView, ArticleCreateView,
    ArticleEditView, ArticleDeleteView
)


urlpatterns = [
    path('', IndexView.as_view(), name='article-index'),
    path('<int:article_id>/', DetailView.as_view(), name="article-detail"),
    path('edit/<int:article_id>/', ArticleEditView.as_view(), name="article-edit"),
    path('delete/<int:article_id>/', ArticleDeleteView.as_view(), name="article-delete"),
    path('create/', ArticleCreateView.as_view(), name="article-create"),
]