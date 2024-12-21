from django.contrib import admin 
from blog.models import Tag, Post
from blog.models import Category, Page 
from django_summernote.admin import SummernoteModelAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe


# adminisntrador de tags
@admin.register(Tag)
# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'id', 'name',  'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('name',),   # preenche o slug com o name ou seja, o slug vai pegar  o valor do name 
                           
    }


# adminisntrador de categorias
@admin.register(Category)
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'id', 'name',  'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('name',),   # preenche o slug com o name ou seja, o slug vai pegar  o valor do name 
                           
    }

# adminisntrador de paginas
@admin.register(Page)
# Register your models here.
class PageAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title', 'is_published',
    list_display_links = 'title',
    search_fields = 'id', 'title',  'content',
    list_per_page = 50
    list_filter = 'is_published',
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {
        'slug': ("title",),   # preenche o slug com o name ou seja, o slug vai pegar  o valor do name 
                           
    }


@admin.register(Post)
# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'title', 'is_published', 'created_by',
    list_display_links = 'title',
    search_fields = 'id', 'title', 'execerpt', 'content',
    list_per_page = 50
    list_filter = 'category','is_published',
    list_editable = 'is_published',
    ordering = '-id',
    readonly_fields = ('created_at','updated_at','created_by', 'updated_by',
                       'link',)
    prepopulated_fields = {
        'slug': ("title",),   # preenche o slug com o name ou seja, o slug vai pegar  o valor do name 
                           
    }

    autocomplete_fields = 'category', 'tags',

    def link(self, obj):
        if not obj.pk:
            return '-'
        url_do_post = obj.get_absolute_url() # url do post
        safe_link = mark_safe(f'<a target="_blank" href="{url_do_post}">Ver post</a>') # mark_safe - para deixar o link seguro
        return  safe_link

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user # Salva o usuário que editou o post
        else:
            obj.created_by = request.user # Salva o usuário que criou o post
        obj.save()