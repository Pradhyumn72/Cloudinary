from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage,RawMediaCloudinaryStorage,VideoMediaCloudinaryStorage

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=40)
    img=models.ImageField(upload_to='images/',storage=MediaCloudinaryStorage)
    document=models.FileField(upload_to='file/',storage=RawMediaCloudinaryStorage)
    audio=models.FileField(upload_to='audio/',storage=VideoMediaCloudinaryStorage)
    video=models.FileField(upload_to='video/',storage=VideoMediaCloudinaryStorage)
    
    def __str__(self):
        return self.name + " " + str(self.img) +" "+ str(self.document)+" "+str(self.audio)+" "+ str(self.video)