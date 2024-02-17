# blog/models.py
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def can_edit(self, user):
        return user == self.author or user.is_staff

    def can_delete(self, user):
        return user.is_staff


class EditorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Tambahkan atribut profil editor sesuai kebutuhan
