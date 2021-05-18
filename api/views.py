from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated


from app.core.pagination import CustomNumberPagination
from app.core.auth import CustomTokenAuthentication
from .serializers import (
    MomoSerializer,
)
from .models import (
    Momo,
)

class HealthView(APIView):
    def get(self, request):
        return Response([], 200)

class MomoViewSet(ViewSet):
    serializer_class = MomoSerializer
    queryset = Momo.objects.all()
    authentication_classes = [CustomTokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    pagination_class = CustomNumberPagination
