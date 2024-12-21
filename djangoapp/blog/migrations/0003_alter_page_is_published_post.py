# Generated by Django 5.1.4 on 2024-12-14 02:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='is_published',
            field=models.BooleanField(default=False, help_text='Este campo precisa ser marcado para que o página seja publicada.'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, default='', max_length=200, null=True, unique=True)),
                ('execerpt', models.CharField(max_length=130)),
                ('is_published', models.BooleanField(default=False, help_text='Este campo precisa ser marcado para que o post seja publicado.')),
                ('content', models.TextField()),
                ('cover', models.ImageField(blank=True, default='', upload_to='assets/cover/%Y/%m/')),
                ('cover_in_post_content', models.BooleanField(default=True, help_text='Este campo precisa ser marcado para que a imagem de capa seja mostrada no conteúdo do post.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
                ('tags', models.ManyToManyField(blank=True, default='', to='blog.tag')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
