# from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View


# Class based view
class PingView(View):
    def get(self, request):
        ping = {"ping": "pong"}
        return JsonResponse(ping)
