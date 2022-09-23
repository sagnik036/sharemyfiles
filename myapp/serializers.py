import shutil
from rest_framework import serializers
from .models import *

class FileListSerilizer(serializers.Serializer):
    files = serializers.ListField(
        child = serializers.FileField(
            max_length = 1000000,
            allow_empty_file = False,
            use_url = False
        )
    )
    folder = serializers.CharField(required = False)

    def zip_files(self,folder):
        shutil.make_archive(f"public/static/zip/{folder}",'zip','https://sharemyfiles.herokuapp.com/public/static/{folder}')

    def create(self , validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        files_objs = []
        for file in files:
            files_obj = Files.objects.create(
                folder = folder,
                file = file
            )
            files_objs.append(files_obj)
        
        self.zip_files(folder.uid)
        
        link = 'http://127.0.0.1:8000/media/zip/'
        return {'files' : {} , 'folder' : link + str(folder.uid)+'.zip'}