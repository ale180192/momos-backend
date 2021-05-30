from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class AbstractMomo(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="momos")
    user = models.ForeignKey(to=User, related_name="user", null=True, on_delete=models.SET_NULL)
    is_public = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Momo(AbstractMomo):
    pass