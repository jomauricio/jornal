# Generated by Django 4.2 on 2023-05-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0008_noticia_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='likes',
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
