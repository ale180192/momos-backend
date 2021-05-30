from django.contrib.auth import get_user_model
from django.db.models import ObjectDoesNotExist
from rest_framework.exceptions import APIException
from rest_framework.serializers import (
    ModelSerializer,
)

from .models import (
    Momo,
)

User = get_user_model()

class MomoSerializer(ModelSerializer):
    class Meta:
        model = Momo
        fields = ['name', 'picture']

