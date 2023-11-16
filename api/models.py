from django.db import models
import datetime, os
# Create your models here.

def filepathLogo(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('Logo', filename)

def filepathBG(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('BG', filename)

def filepathQR(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('QR', filename)

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

class Media (models.Model) :

    logo = models.FileField(upload_to=filepathLogo, null=True, blank=True)
    bg = models.FileField(upload_to=filepathBG, null=True, blank=True)
    qr = models.FileField(upload_to=filepathQR, null=True, blank=True)
    code = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
       return self.code