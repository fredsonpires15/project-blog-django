from django.db import models # type: ignore
from utils.model_validators import validate_png
from utils.images import resize_image


class MenuLink(models.Model):
    class Meta:
        verbose_name = "Menu Link"
        verbose_name_plural = "Menu Links"

    text = models.CharField(max_length=50) # Texto do menu link com máximo de 50 caracteres
    url_or_path = models.CharField(max_length=2048) # URL do link ou caminho do link com máximo de 2048 caracteres
    new_tab = models.BooleanField(default=False) # Indica se o link deve ser aberto em uma nova aba
    site_setup = models.ForeignKey(
        'SiteSetup', on_delete=models.CASCADE, blank=True, null=True,
        default=None
        
        )
    
    def __str__(self): # Retorna o texto do menu link
        return self.text


class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup do Site'
        verbose_name_plural = 'Setup do Site'

    title = models.CharField(max_length=65) # Exibe o titulo com 50 caracteres
    description = models.CharField( max_length=255) # Exibe a descricao com 255 caracteres

    show_header = models.BooleanField(default=True) # Exibe o cabecalho
    show_search = models.BooleanField(default=True) # Exibe a barra de pesquisa
    show_menu = models.BooleanField(default=True) # Exibe o menu
    show_footer = models.BooleanField(default=True) # Exibe o rodape
    show_description = models.BooleanField(default=True) # Exibe a descricao
    show_pagination = models.BooleanField(default=True) # Exibe a paginacao

    favicon = models.ImageField(       # carrega uma imagem de favicon (icon)
        upload_to='assets/favicon/%Y/%m/', 
        default='', 
        blank=True,
        validators=[validate_png,]    
    )

    def save(self, *args, **kwargs): # Salva o favicon
        current_favicon_name = str(self.favicon.name) # Nome do favicon atual
        super().save(*args, **kwargs)

        favicon_changed = False

        if self.favicon: # Verifica se o favicon foi alterado
            favicon_changed = current_favicon_name != str(self.favicon.name) # Verifica se o favicon é diferente
        
        if favicon_changed: # Verifica se o favicon esta sendo alterado
            resize_image(self.favicon,32)  # Redimensiona o favicon

        #resize_image(self.favicon, new_width=32, optimize=True, quality=60)

    def __str__(self):
        return self.title
    #image = models.ImageField(upload_to='site_setup', null=True, blank=True)