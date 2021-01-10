from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2048)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True,
        width_field='width_field',
        height_field='height_field',
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    draft = models.BooleanField(default=False)  # черновик публикации

    def __str__(self):
        return f'{self.id}. {self.title}'

    class Meta:
        ordering = ['-timestamp', '-updated']
