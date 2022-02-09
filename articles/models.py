from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    # scopes = models.ManyToManyField('Theme', related_name='article', through="ArticleTheme")
    # news = models.ManyToOneRel()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Theme(models.Model):
    theme = models.CharField(max_length=50, verbose_name='Темы')
    article = models.ManyToManyField(Article, related_name='scopes', through='ArticleTheme')
    #news = models.ManyToOneRel()

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.theme


class ArticleTheme(models.Model):
    article = models.ForeignKey(Article, related_name='news', on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, related_name='news', on_delete=models.CASCADE)
    main = models.BooleanField(verbose_name='Главная тема')
