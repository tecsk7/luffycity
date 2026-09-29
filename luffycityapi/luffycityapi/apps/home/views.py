


from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
#log diaoyong
import logging
logger = logging.getLogger("django")

class HomeAPIView(APIView):
    def get(self,request):
        print("hello")
        logger.debug('debug message')
        logger.info('info message')
        brother = ['jack', 'lucy']
        return Response(brother,status=status.HTTP_200_OK)