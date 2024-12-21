from django.shortcuts import render # type: ignore
from django.core.paginator import Paginator # type: ignore
from blog.models import Post




POSTS_PER_PAGE = 9

# Create your views here.
def index(request):

    posts = Post.objectos.get_published()
        
    

    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, 
        'blog/pages/index.html',

        {
            'page_obj': page_obj
        }
        
    )

def page(request, slug):
    return render(
        request, 
        'blog/pages/page.html',

        {
            #'page_obj': page_obj
        }
        
    )

def post(request, slug):
    post = (Post.objectos.get_published()
             .filter(slug=slug)
             .first()
     )

    return render(
        request, 
        'blog/pages/post.html',

        {
            'post': post
        }    
    )


def created_by(request, author_id):

    posts = Post.objectos.get_published()\
        .filter(created_by__pk=author_id)
        

    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, 
        'blog/pages/index.html',

        {
            'page_obj': page_obj
        }
        
    )


def category(request, slug):

    posts = Post.objectos.get_published()\
        .filter(category__slug=slug)
        

    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, 
        'blog/pages/index.html',

        {
            'page_obj': page_obj
        }
        
    )