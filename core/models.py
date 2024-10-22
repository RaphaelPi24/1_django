from django.db import models


class Post(models.Model):
    email = models.EmailField()
