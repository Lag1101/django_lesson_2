from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    # parent_comment = models.ForeignKey('Comment', on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'pk': self.article.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='gallery')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
