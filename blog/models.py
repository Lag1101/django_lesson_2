from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from markdown import markdown


class Article(models.Model):
    header = models.CharField(max_length=128)
    markdown = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def save(self, **kwargs):
        self.html = markdown(self.markdown)
        super(Article, self).save()

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'pk': self.pk})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'pk': self.article.pk})
