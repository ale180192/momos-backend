from django.urls import path
from rest_framework.authtoken import views as drf_token_view

app_name = 'momoauth'
urlpatterns = [
    path('api/v1/auth/token',
        drf_token_view.ObtainAuthToken.as_view(),
        name='token'),
]