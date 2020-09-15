from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
# Create your views here.

class RegisterView(View):

    def get(self,request):
        return render(request, 'register.html')
    def post(self,request):
        pass