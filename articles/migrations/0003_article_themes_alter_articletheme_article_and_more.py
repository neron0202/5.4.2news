# Generated by Django 4.0.2 on 2022-02-06 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_theme_alter_article_options_articletheme'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='themes',
            field=models.ManyToManyField(related_name='scopes', through='articles.ArticleTheme', to='articles.Theme'),
        ),
        migrations.AlterField(
            model_name='articletheme',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='articletheme',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='articles.theme'),
        ),
    ]
