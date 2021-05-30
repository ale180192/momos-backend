from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    MomoViewSet,
    HealthView,
)

router = SimpleRouter()
router.register("momos", MomoViewSet, basename="momos")

app_name = 'api'
urlpatterns = [
    path('', HealthView.as_view(), name='health'),
]
urlpatterns += router.urls