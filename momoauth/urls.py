from django.urls import path

from .views import CustomObtainAuthToken

app_name = 'momoauth'
urlpatterns = [
    path('token',
        CustomObtainAuthToken.as_view(),
        name='token'),
]