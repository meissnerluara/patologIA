from django.db import models
import uuid

class VideoModel(models.Model):
    Id_Video = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Description_Of_Video = models.CharField(max_length=1000)
    Video_File = models.FileField(upload_to='videos/')
    Date_Of_Upload = models.DateField(blank=True, null=True)
    Creators_Information = models.ForeignKey('AccountsApp.CustomUserModel', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.Description_Of_Video
