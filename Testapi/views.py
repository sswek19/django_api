from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import *
# from django.core.context_processors import csrf
# from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import datetime,json
# Create your views here.
from sweksha.Django_api.Testapi.models import User_Detail


@api_view(['GET','POST'])
def labdata(request):
    if request.method=='POST':
        if request.data:
            print(request.data)
            user_id=request.data['user_id']
            user_name=request.data['user_name']
            tz=request.data['tz']
            start_time=request.data['start_time']
            end_time=request.data['end_time']
            start_t=datetime.datetime.strptime(start_time, '%b %d %Y %H:%M%p')
            end_t=datetime.datetime.strptime(end_time, '%b %d %Y %H:%M%p')
            # print(t)
            user_details = User_Detail.objects.create(user_id=user_id,user_name=user_name,tz=tz,start_time=start_t,end_time=end_t)
            user_details.save()
            return Response('data store successfully',status=200)
    elif request.method=='GET':

        
        tempdict={}
        l=[]
        l1=[]
        data_list=[]
        user_details=User_Detail.objects.all()
        d=User_Detail.objects.values_list('user_name', flat=True).distinct()
        user_list=[user for user in d]
        
       
        
        for user in user_list:
            data=User_Detail.objects.filter(user_name=user)
    
            l.append({'id':data[0].user_id,'name':data[0].user_name,'tz':data[0].tz})
            for U_item in data:
                l1.append({'start_time':U_item.start_time,'end_time':U_item.end_time})
           
            l[0]['activity']=l1    
            data_list.append(l[0])
        contant={}
        contant["ok"]="true"
        contant["member"]=data_list
        return Response(contant,status=200)
    else:
        return Response('',status=404)

