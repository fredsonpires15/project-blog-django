from django.db import models # type: ignore
from utils.rands import slogify_new
from django.contrib.auth.models import User
from utils.images import resize_image
from django.urls import reverse
from django_summernote.models import AbstractAttachment






class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name
        
        current_file_name = str(self.file.name) # Nome do cover atual
        super_save = super().save(*args, **kwargs)

        file_changed = False

        if self.file: # Verifica se o cover foi alterado
            file_changed = current_file_name != str(self.file.name) # Verifica se o cover é diferente
        
        if file_changed: # Verifica se o cover esta sendo alterado
            resize_image(self.file,900, True, 70)  # Redimensiona o cover

        #resize_image(self.cover, new_width=32, optimize=True, quality=60)

        return super_save


# criar tags de posts
class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=200)
    slug = models.SlugField(
        unique=True, default=None, 
        blank=True, null=True,
        max_length=200
    )
    
    def save(self, *args, **kwargs): # Salva o slug
        if not self.slug:
            self.slug = slogify_new(self.name, 4)

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

# criar categorias de posts    
class Category(models.Model): 
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)
    slug = models.SlugField(
        unique=True, default=None, 
        blank=True, null=True,
        max_length=200
    )

    def save(self, *args, **kwargs): # Salva o slug
        if not self.slug:
            self.slug = slogify_new(self.name, 4)

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class PostManager(models.Manager):  # Usar pots manager para evitar repetição do codigo
    def get_published(self):
        return self\
            .filter(is_published=True)\
            .order_by('-id')

# criar paginas de posts 
class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True, default="", 
        blank=True, null=False,
        max_length=200
    )

    objectos = PostManager()

    content = models.TextField()
    is_published = models.BooleanField(
        default=False,
        help_text="Este campo precisa ser marcado para que o página seja publicada.",
    )

    def get_absolute_url(self): # retorna a url do post
        if not self.is_published:
            return reverse('blog:index')
        return reverse('blog:page', args=(self.slug,))

    def save(self, *args, **kwargs): # Salva o slug
        if not self.slug:
            self.slug = slogify_new(self.title, 4)

        return super().save(*args, **kwargs)
    def __str__(self):
        return self.title



    

class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    objectos = PostManager()

    title = models.CharField(max_length=200) # título do post
    slug = models.SlugField(       # slug do post que serve para identificar o post
        unique=True, default="", 
        blank=True, null=True,
        max_length=200
    )
    
    execerpt = models.CharField(max_length=130) # resumo do post mostrado na home

    
    is_published = models.BooleanField(     # verifica se o post foi publicado
        default=False,
        help_text="Este campo precisa ser marcado para que o post seja publicado.",
    )

    content = models.TextField()

    cover = models.ImageField(       # carregar uma imagem de capa (cover) para o post
        upload_to='assets/cover/%Y/%m/', 
        default='', 
        blank=True,    
    )

    cover_in_post_content = models.BooleanField(     # verifica se a imagem de capa deve ser mostrada no conteúdo do post
        default=True,
        help_text="Este campo precisa ser marcado para que a imagem de capa seja mostrada no conteúdo do post.",
    )

    created_at = models.DateTimeField(auto_now_add=True) # salvar a data de criação do post
    created_by = models.ForeignKey(     # salvar o usuário que criou o post
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='page_created_by',
    )
    updated_at = models.DateTimeField(auto_now=True) # salvar a data de atualização do post
    updated_by = models.ForeignKey(     # salvar o usuário que atualizou o post
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='page_updated_by',
    )

    tags = models.ManyToManyField(Tag, blank=True, default="") # cria uma relação de muitos para muitos, fazendo com que o post possa ter muitas tags

    category = models.ForeignKey(       # cria uma relação de um para muitos, faz com que muitos posts possam pertencer a uma mesma categoria
        Category,
        on_delete=models.SET_NULL,
        blank=True,                
        null=True,
        default=None,
    )
    
    def get_absolute_url(self): # retorna a url do post
        if not self.is_published:
            return reverse('blog:index')
        return reverse('blog:post', args=(self.slug,))

    def save(self, *args, **kwargs): # Salva o slug
        if not self.slug:       
            self.slug = slogify_new(self.title, 4)
        
        # configurar o tamanho da imagem de capa
        current_cover_name = str(self.cover.name) # Nome do cover atual
        super_save = super().save(*args, **kwargs)

        cover_changed = False

        if self.cover: # Verifica se o cover foi alterado
            cover_changed = current_cover_name != str(self.cover.name) # Verifica se o cover é diferente
        
        if cover_changed: # Verifica se o cover esta sendo alterado
            resize_image(self.cover,900, True, 70)  # Redimensiona o cover

        #resize_image(self.cover, new_width=32, optimize=True, quality=60)

        return super_save
    
    def __str__(self) -> str:
        return self.title
