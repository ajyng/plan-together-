from django.db import models
from django.conf import settings
from django.urls import reverse
from django.shortcuts import resolve_url

class Post(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_post')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='community/image/%Y/%M/%D', default='default.jpeg')
    
    view_count = models.PositiveIntegerField(default=0)

    total_user = models.PositiveIntegerField()
    apply_user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='apply_user_post')


    def get_absolute_url(self):
        return reverse("community:post_detail", args=[self.pk])

    def is_applied(self, user):
        return self.apply_user.filter(pk=user.pk).exists()

    