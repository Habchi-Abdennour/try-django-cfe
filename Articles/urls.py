from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("article/",views.search,name='article_search'),
    path("create/",views.create_article,name='create_article'),
    path("article/<int:article_id>/",views.article_Detail,name='article_Detail'),
    
]
