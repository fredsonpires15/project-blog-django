
from django.urls import path # type: ignore
from blog.views import index, page, post, created_by, category

app_name = 'blog'

urlpatterns = [
    path('',  index, name='index'),
    path('page/',  page, name='page'),
    path('post/<slug:slug>/',  post, name='post'),
    path('created_by/<int:author_id>/',  created_by, name='created_by'),
    path('category/<slug:slug>/',  category, name='category'),
]

