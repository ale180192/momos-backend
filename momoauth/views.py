from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken


class CustomObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        resp = super().post(request, *args, **kwargs)
        return resp
