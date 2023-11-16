from django.db import models
import datetime, os
# Create your models here.

def filepathPDF(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('PDF/PDF', filename)

def filepathPDFLogo(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('PDF/Logo', filename)

class PDF (models.Model) :

    logo = models.FileField(upload_to=filepathPDFLogo, null=True, blank=True)
    pdf = models.FileField(upload_to=filepathPDF, null=True, blank=True)
    code = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
       return self.code