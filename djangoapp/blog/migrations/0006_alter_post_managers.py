# Generated by Django 5.1.4 on 2024-12-16 21:22

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_postattachment'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('objectos', django.db.models.manager.Manager()),
            ],
        ),
    ]
