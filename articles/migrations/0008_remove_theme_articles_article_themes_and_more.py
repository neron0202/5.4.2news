# Generated by Django 4.0.2 on 2022-02-09 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_remove_theme_article_theme_articles_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='articles',
        ),
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
