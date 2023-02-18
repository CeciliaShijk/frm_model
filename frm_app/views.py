#django返回数据
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
#django自带的视图
from django.views import View
#djangoframework的视图(好用)
from rest_framework.views import APIView
#djangoframework序列化器
from rest_framework import serializers
#djangoframeword返回
from rest_framework.response import Response

#表
from frm_app.models import User

#序列化类
class userserializers(serializers.Serializer):
    """serializers for User"""
    companyname = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()



class Users(APIView):
    def get(self,request):
        print(request.GET.dict())
        query=User.objects.all()
        print(query)
        query_data=userserializers(instance=query,many=True)
        print(query_data.data)
        return Response(query_data.data)

    def post(self,request):
        #添加
        print(request.data)
        serobject=userserializers(data=request.data)
        #校验
        try:
            serobject.is_valid(raise_exception=True)
            User.objects.create(**serobject.validated_data)
            return HttpResponse('true')
        except:
            return HttpResponse(serobject.errors)

