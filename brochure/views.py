from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from rest_framework.decorators import api_view
from django.http import JsonResponse
from reportlab.lib.units import mm
from PIL import Image, ImageDraw, ImageColor, ImageFont
from .models import PDF
from qrcode import *
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer, RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
import pymongo, time, uuid, datetime, requests, qrcode, os

def index (request) :
    return redirect ('https://gofer.et')

@api_view(['POST'])
def upload_pdf (request) :

    client = pymongo.MongoClient("mongodb+srv://dbonelink:S7wRp1NZWxp2zsjz@onelink.gfjk5uq.mongodb.net/?retryWrites=true&w=majority")
 
    # Database Name
    db = client["OneLink"]
    # Collection Name
    col = db["brochure"]

    if request.method == 'POST' :

        code = request.POST.get('code')
        name = request.POST.get('name')
        logo = request.FILES.get('logo')
        pdf = request.FILES.get('pdf')
        duration = request.POST.get('duration')
        sub_link = request.POST.get('sub_link')
        back_color = request.POST.get('back_color')
        fill_color = request.POST.get('fill_color')

        back_colors = back_color.split(',')
        front_colors = fill_color.split(',')

        current_date = datetime.date.today()

        #save data
        record = col.find_one({'sub_link': sub_link})
        if record is not None :
            return JsonResponse({
                'result' : 'Sub Link already used.'
            })
        
        pdf = PDF.objects.create (
            logo = logo,
            pdf = pdf,
            code = code
        )

        record = {
            'name' : name,
            'code' : code,
            'duration' : duration,
            'sub_link' : sub_link,
            'register_date' : str(current_date)
        }

        col.insert_one(record)

        main_img = Image.new( mode = "RGB", size = (480, 550), color = (int(back_colors[0]), int(back_colors[1]), int(back_colors[2])))
        logo_url = Image.open('/home/nathanel/Documents/Projects/OneLink/OneLink/media/' + str(PDF.objects.get(code=code).logo))
        logo_url = logo_url.resize((80,80))
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        qr.add_data('https://q.gofer.et/'+ sub_link)
        qr.make(fit = True)
        img = qr.make_image(image_factory=StyledPilImage,eye_drawer=RoundedModuleDrawer(radius_ratio=1.2), module_drawer=CircleModuleDrawer(), 
                            color_mask=SolidFillColorMask(back_color=(int(back_colors[0]), int(back_colors[1]), int(back_colors[2])), 
                            front_color=(int(front_colors[0]),int(front_colors[1]),int(front_colors[2]))), size=50 * mm).convert('RGB')
        
        main_img.paste(img, (50, 100))
        main_img.paste(logo_url, (190, 20), mask=logo_url)
        draw = ImageDraw.Draw(main_img)
        myFont = ImageFont.truetype('/home/nathanel/Documents/Projects/OneLink/OneLink/static/Poppins-SemiBold.ttf', 16)
        draw.text((130, 480), 'https://q.gofer.et/'+ sub_link, font=myFont, fill =(int(front_colors[0]),int(front_colors[1]),int(front_colors[2])))

        img_name = 'qr-brochure-'+ name + str(time.time()) + '.png'
        main_img.save(settings.MEDIA_ROOT + '/' + img_name)
        
        return JsonResponse({
            'result' : 'Uploading is successful.'
        })
    
    return JsonResponse({
        'result' : 'Uploading is failed.'
    })

@api_view(['PATCH'])
def update_pdf (request) :

    client = pymongo.MongoClient("mongodb+srv://dbonelink:S7wRp1NZWxp2zsjz@onelink.gfjk5uq.mongodb.net/?retryWrites=true&w=majority")
 
    # Database Name
    db = client["OneLink"]
    # Collection Name
    col = db["brochure"]

    if request.method == 'PATCH' :

        code = request.POST.get('code')
        name = request.POST.get('name')
        logo = request.FILES.get('logo')
        pdf = request.FILES.get('pdf')
        duration = request.POST.get('duration')
        sub_link = request.POST.get('sub_link')

        brochure = PDF.objects.get(code=code)
        if logo != None :
            brochure.logo = logo
        if pdf != None :
            brochure.pdf = pdf
        brochure.save()

        if name != '' :
            col.find_one_and_update({'code': code},{'$set': { "name" : name}})
        if duration != '' :
            col.find_one_and_update({'code': code},{'$set': { "duration" : duration}})
        if sub_link != '' :
            record = col.find_one({'sub_link': sub_link})
            if record is not None :
                return JsonResponse({
                    'result' : 'Sub Link already used.'
                })
            col.find_one_and_update({'code': code},{'$set': { "sub_link" : sub_link}})

        return JsonResponse({
            'result' : 'Patch is successful.'
        })
    
    return JsonResponse({
        'result' : 'Patch is failed.'
    })

@api_view(['DELETE'])
def delete_pdf (request) :
    
    client = pymongo.MongoClient("mongodb+srv://dbonelink:S7wRp1NZWxp2zsjz@onelink.gfjk5uq.mongodb.net/?retryWrites=true&w=majority")
 
    # Database Name
    db = client["OneLink"]
    # Collection Name
    col = db["brochure"]

    if request.method == 'DELETE' :

        code = request.POST.get('code')
        record = PDF.objects.filter(code=code).all()
        record.delete()

        col.delete_one({'code':code})
        return JsonResponse({
            'result' : 'Delete is successful.'
        })
    
    return JsonResponse({
        'result' : 'Delete is failed.'
    })

def result (request, subLink) :

    client = pymongo.MongoClient("mongodb+srv://dbonelink:S7wRp1NZWxp2zsjz@onelink.gfjk5uq.mongodb.net/?retryWrites=true&w=majority")
 
    # Database Name
    db = client["OneLink"]
    # Collection Name
    col = db["brochure"]

    record = col.find_one({'sub_link': subLink})
    if record is None :
        return render(request, '404.html')
    
    current_date = datetime.date.today()
    difference = (current_date - datetime.datetime.strptime(record.get('register_date'), '%Y-%m-%d').date()).days
    if int(difference) > int(record.get('duration')) :
        return render(request, '404.html')
    
    pdf_ = PDF.objects.get(code=record.get('code'))
    return render (request, 'brochure.html', {
        'name' : record.get('name'),
        'logo' : pdf_.logo,
        'pdf' : pdf_.pdf
    })