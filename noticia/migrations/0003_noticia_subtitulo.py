# Generated by Django 4.1.3 on 2022-12-03 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0002_alter_autor_options_alter_autor_data_nascimento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='subtitulo',
            field=models.CharField(default='', max_length=200, verbose_name='Subtitulo'),
            preserve_default=False,
        ),
    ]
