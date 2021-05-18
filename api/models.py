from django.db import models


class Momo(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="momos")