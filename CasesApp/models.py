from django.db import models
import uuid

class CasesModel(models.Model):
    IDCase = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    CaseStudyNumber = models.IntegerField()
    CaseStudyFileName = models.CharField(max_length=500)
    CaseStudyFile = models.FileField(upload_to='pdf_files/')
    
    def __str__(self):
        return self.CaseStudyFileName
