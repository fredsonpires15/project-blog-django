from django.contrib import admin
from django.http.request import HttpRequest
from .models import MenuLink, SiteSetup



# @admin.register(MenuLink)
# class MenuLinkAdmin(admin.ModelAdmin):
#     list_display = ( 'id','text', 'url_or_path') # Exibe o id, o texto e a url ou caminho do link
#     list_display_links = ('id','text', 'url_or_path') # Exibe o id, o texto e a url ou caminho do link
#     search_fields = ('id', 'text', 'url_or_path') # Busca pelo id, pelo texto e pela url ou caminho do link

class MenuLinkInline(admin.TabularInline): # Adiciona uma linha para cada menu link
    model = MenuLink    # Define o modelo para o menu link
    extra = 1       # Define o número de linhas adicionais

@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = MenuLinkInline,
    def has_add_permission(self, request) -> bool: # Verifica se o usuário tem permissão para adicionar um novo registro 
        return not SiteSetup.objects.exists() # Verifica se não há nenhum registro na tabela SiteSetup para permitir a criação de um novo registro se nenhuma existir 
    
