from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.parsers import MultiPartParser
from django.shortcuts import render
from rest_framework.generics import GenericAPIView


class handleFileUpload(GenericAPIView):
    serializer_class = FileListSerilizer
    parser_classes = [MultiPartParser]

    def get(self, request):
        my_msg = "this is an API created using django-rest-framework, you can use this api to store and share your files via link that will automatically genrated and return by the API as a response, you can use this api for backend of your application , or you can use it in postman to  check the working of it"
        response = {
            "message": my_msg
        }
        return Response(response,status=200)
    def post(self, request):
        data = request.data
        serializer = FileListSerilizer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 200,
                'message': "File Upload Succesfully",
                'data': serializer.data
            }
            return Response(response, status=200)

        response = {
            'status': 400,
            'message': "File Upload Failed",
            'data': serializer.errors
        }
        return Response(response, status=400)
