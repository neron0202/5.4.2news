# Generated by Django 4.0.2 on 2022-02-09 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_remove_article_scopes_theme_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='article',
        ),
        migrations.AddField(
            model_name='theme',
            name='articles',
            field=models.ManyToManyField(related_name='themes', through='articles.ArticleTheme', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='articletheme',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='articletheme',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.theme'),
        ),
    ]