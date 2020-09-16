import re
import logging
from django.contrib.auth.views import login
from django.shortcuts import render
from django import http
from django.views import View
from register.models import User
# from rest_framework.views import APIView
# Create your views here.
logger = logging.getLogger('django')


class RegisterView(View):

    def get(self,request):
        return render(request, 'register.html')
    def post(self,request):
        body = request.POST
        username = body.get("username")
        password = body.get("password")
        password2 = body.get("password2")
        mobile = body.get("mobile")
        sms_code = body.get("sms_code")
        allow = body.get("allow")
        valie = [username, password,password2,mobile,allow,allow]

        if not all(valie):
            return http.HttpResponseForbidden('数据错误')
        if not allow=='on':
            return http.HttpResponseForbidden('验证码错误')
        if not re.match(r'[A-Za-z0-9\w]{5,10}', username):
            return http.HttpResponseForbidden('用户字段不符')
        if not re.match(r'[A-Za-z0-9]{8,20}',password):
            return http.HttpResponseForbidden('密码长度不符')
        if not password==password2:
            return http.HttpResponseForbidden('验证密码错误')
        try:
            user = User.objects.create_user(username=username,password=password,mobile=mobile)
            login(request, user)
        except Exception as e:
            logger.error(e)
            return http.HttpResponseForbidden('注册失败')

        return render(request, 'index.html')
