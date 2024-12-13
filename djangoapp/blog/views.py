from django.shortcuts import render # type: ignore
from django.core.paginator import Paginator # type: ignore


posts = list(range(1000))
# Create your views here.
def index(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, 
        'blog/pages/index.html',

        {
            'page_obj': page_obj
        }
        
    )

def page(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request, 
        'blog/pages/page.html',

        {
            #'page_obj': page_obj
        }
        
    )

def post(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request, 
        'blog/pages/post.html',

        {
            #'page_obj': page_obj
        }
        
    )