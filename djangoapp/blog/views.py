from django.shortcuts import render # type: ignore
from django.core.paginator import Paginator # type: ignore
from blog.models import Post, Page
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404 



POSTS_PER_PAGE = 9

# Create your views here.
def index(request):

    posts = Post.objectos.get_published()
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404
    
    page_title = page_obj[0].category.name + ' - Categoria - '

    return render(
        request, 
        'blog/pages/index.html',

        {
            'page_obj': page_obj,
            'Page_title': 'Home '
        }
        
    )

def page(request, slug):

    page = (
        Page.objectos
             .filter(slug=slug)
             .filter(is_published=True)
             .first()
     )
    return render(
        request, 
        'blog/pages/page.html',

        {
            'page': page,
            'Page_title': 'Home '
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
            'post': post,
            'Page_title': 'Home '
        }    
    )


def created_by(request, author_id):
    
    posts = Post.objectos.get_published()\
        .filter(created_by__pk=author_id)

    user = User.objects.filter(pk=author_id).first()

    if not user:
        raise Http404()
    
    user_full_name = user.username   
    if (user.first_name):  
        user_full_name = f'{user.first_name} {user.last_name}'

    page_title = f'Posts de {user_full_name} - '
    
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, 
        'blog/pages/index.html',

        {
            'page_obj': page_obj,
            'Page_title': page_title
        }
        
    )


def category(request, slug):

    posts = Post.objectos.get_published()\
        .filter(category__slug=slug)
    

    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404
    
    page_title = page_obj[0].category.name + ' - Categoria - '


    return render(
        request, 
        'blog/pages/index.html',

        {
            'page_obj': page_obj,
            'Page_title': page_title,
        }
        
    )




def tag(request, slug):

    posts = Post.objectos.get_published()\
        .filter(tags__slug=slug)
        

    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404
    
    page_title = page_obj[0].tags.first().name + ' - tag - '

    return render(
        request, 
        'blog/pages/index.html',

        {
            'page_obj': page_obj,
            'Page_title': page_title,
        }
        
    )

def search(request):

    search_value = request.GET.get('search', '').strip() 

    posts = (
        Post.objectos.get_published()\
        .filter(
            # titulo ou execerpt ou content contem o search_value
            Q(title__icontains=search_value) |
            Q(execerpt__icontains=search_value) |
            Q(content__icontains=search_value)

        )[:POSTS_PER_PAGE]
        
    )  



    return render(
        request, 
        'blog/pages/index.html',

        {
            'page_obj': posts,
            'search_value': search_value,
            'page_title': 'Home'
        }   
    )




