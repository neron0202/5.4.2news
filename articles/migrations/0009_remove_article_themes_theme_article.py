# Generated by Django 4.0.2 on 2022-02-09 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_remove_theme_articles_article_themes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='themes',
        ),
        migrations.AddField(
            model_name='theme',
            name='article',
            field=models.ManyToManyField(related_name='scopes', through='articles.ArticleTheme', to='articles.Article'),
        ),
    ]
