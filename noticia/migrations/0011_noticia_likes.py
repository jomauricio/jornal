# Generated by Django 4.2 on 2023-05-16 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0010_remove_noticia_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='likes',
            field=models.SmallIntegerField(blank=True, default=0, null=True, verbose_name='Likes'),
        ),
    ]
