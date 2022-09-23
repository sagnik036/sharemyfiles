from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import MultiPartParser
from django.shortcuts import render
from rest_framework.generics import GenericAPIView

class handleFileUpload(GenericAPIView):
    serializer_class = FileListSerilizer
    parser_classes = [MultiPartParser]
    def post (self,request):
        try:
            data = request.data
            serializer = FileListSerilizer(data = data)
            if serializer.is_valid():
                serializer.save()
                response = {
                    'status' : 200,
                    'message' : "File Upload Succesfully",
                    'data' : serializer.data
                }
                return Response(response,status=200)
            
            response = {
                    'status' : 400,
                    'message' : "File Upload Failed",
                    'data' : serializer.errors
                }
            return Response(response,status=400)

        except Exception as e:
            print(e)
            