from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from rest_framework.decorators import api_view
from django.http import JsonResponse
from reportlab.lib.units import mm
from PIL import Image, ImageDraw, ImageColor, ImageFont
from .models import Media
from qrcode import *
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer, RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
import pymongo, time, uuid, datetime, requests, qrcode, os

def index (request) :
    return redirect ('https://gofer.et')

@api_view(['POST'])
def create (request) :

    client = pymongo.MongoClient("mongodb+srv://dbonelink:S7wRp1NZWxp2zsjz@onelink.gfjk5uq.mongodb.net/?retryWrites=true&w=majority")
 
    # Database Name
    db = client["OneLink"]
    # Collection Name
    col = db["onelink"]

    if request.method == 'POST' :

        code = request.POST.get('code')
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        logo = request.FILES.get('logo')
        duration = request.POST.get('duration')
        sub_link = request.POST.get('sub_link')

        facebook = request.POST.get('facebook')
        facebooks_text = request.POST.get('facebooks_text')
        instagram = request.POST.get('instagram')
        instagrams_text = request.POST.get('instagrams_text')
        twitter = request.POST.get('twitter')
        twitters_text = request.POST.get('twitters_text')
        telegram = request.POST.get('telegram')
        telegrams_text = request.POST.get('telegrams_text')
        youtube = request.POST.get('youtube')
        youtubes_text = request.POST.get('youtubes_text')
        pinterest = request.POST.get('pinterest')
        pinterests_text = request.POST.get('pinterests_text')
        tiktok = request.POST.get('tiktok')
        tiktoks_text = request.POST.get('tiktoks_text')
        google = request.POST.get('google')
        google_text = request.POST.get('googleText')
        googles_text = request.POST.get('googles_text')

        website = request.POST.get('website')
        web_text = request.POST.get('webText')
        websites_text = request.POST.get('websites_text')
        phone = request.POST.get('phone')
        phone_text = request.POST.get('phoneText')
        phones_text = request.POST.get('phones_text')
        email = request.POST.get('email')
        email_text = request.POST.get('emailText')
        emails_text = request.POST.get('emails_text')

        location = request.POST.get('location')
        loc_text = request.POST.get('locText')
        locations_text = request.POST.get('locations_text')
        custom_link = request.POST.get('custom-link')
        custom_link_text = request.POST.get('custom-linkText')
        custom_links_text = request.POST.get('custom_links_text')

        type = request.POST.get('type')
        background_type = request.POST.get('bg-type')
        background_image = request.FILES.get('bg-image')
        background_color = request.POST.get('bg-color')
        font_color = request.POST.get('font-color')
        
        back_color = request.POST.get('back_color')
        fill_color = request.POST.get('fill_color')

        back_colors = back_color.split(',')
        front_colors = fill_color.split(',')

        current_date = datetime.date.today()

        # Save data
        record = col.find_one({'sub_link': sub_link})
        if record is not None :
            return JsonResponse({
                'result' : 'Sub Link already used.'
            })
        if background_type == 'image' :
            media = Media.objects.create(
                logo = logo,
                bg = background_image,
                code = code
            )
            #Save text data
            record = {
                'code' : code,
                'name' : name,
                'desc' : desc,
                'duration' : duration,
                'sub_link' : sub_link,
                'facebook' : facebook,
                'facebooks_text' : facebooks_text,
                'instagram' : instagram,
                'instagrams_text' : instagrams_text,
                'twitter' : twitter,
                'twitters_text' : twitters_text,
                'telegram' : telegram,
                'telegrams_text' : telegrams_text,
                'youtube' : youtube,
                'youtubes_text' : youtubes_text,
                'pinterest' : pinterest,
                'pinterests_text' : pinterests_text,
                'tiktok' : tiktok,
                'tiktoks_text' : tiktoks_text,
                'google' : google,
                'google_text' : google_text,
                'googles_text' : googles_text,
                'website' : website,
                'web_text' : web_text,
                'websites_text' : websites_text,
                'phone' : phone,
                'phone_text' : phone_text,
                'phones_text' : phones_text,
                'email' : email,
                'email_text' : email_text,
                'emails_text' : emails_text,
                'location' : location,
                'loc_text' : loc_text,
                'locations_text' : locations_text,
                'custom_link' : custom_link,
                'custom_link_text' : custom_link_text,
                'custom_links_text' : custom_links_text,
                'type' : type,
                'background_type' : background_type,
                'background_image' : 'Yes',
                'background_color' : 'None',
                'font_color' : font_color,
                'register_date' : str(current_date)

            }
            col.insert_one(record)

        else :
            media = Media.objects.create(
                logo = logo,
                code = code
            )
            #Save text data
            record = {
                'code' : code,
                'name' : name,
                'desc' : desc,
                'duration' : duration,
                'sub_link' : sub_link,
                'facebook' : facebook,
                'facebooks_text' : facebooks_text,
                'instagram' : instagram,
                'instagrams_text' : instagrams_text,
                'twitter' : twitter,
                'twitters_text' : twitters_text,
                'telegram' : telegram,
                'telegrams_text' : telegrams_text,
                'youtube' : youtube,
                'youtubes_text' : youtubes_text,
                'pinterest' : pinterest,
                'pinterests_text' : pinterests_text,
                'tiktok' : tiktok,
                'tiktoks_text' : tiktoks_text,
                'google' : google,
                'google_text' : google_text,
                'googles_text' : googles_text,
                'website' : website,
                'web_text' : web_text,
                'websites_text' : websites_text,
                'phone' : phone,
                'phone_text' : phone_text,
                'phones_text' : phones_text,
                'email' : email,
                'email_text' : email_text,
                'emails_text' : emails_text,
                'location' : location,
                'loc_text' : loc_text,
                'locations_text' : locations_text,
                'custom_link' : custom_link,
                'custom_link_text' : custom_link_text,
                'custom_links_text' : custom_links_text,
                'type' : type,
                'background_type' : background_type,
                'background_image' : 'None',
                'background_color' : background_color,
                'font_color' : font_color,
                'register_date' : str(current_date)

            }
            col.insert_one(record)
        
        main_img = Image.new( mode = "RGB", size = (480, 550), color = (int(back_colors[0]), int(back_colors[1]), int(back_colors[2])))
        logo_url = Image.open('/home/nathanel/Documents/Projects/OneLink/OneLink/media/' + str(Media.objects.get(code=code).logo))
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

        img_name = 'qr-link-'+ name + str(time.time()) + '.png'
        main_img.save(settings.MEDIA_ROOT + '/' + img_name)

        return JsonResponse({
            'result': 'Successful.'
        })
    return JsonResponse({
            'result': 'Failed.'
        })

@api_view(['PATCH'])
def update (request) :

    client = pymongo.MongoClient("mongodb+srv://dbonelink:S7wRp1NZWxp2zsjz@onelink.gfjk5uq.mongodb.net/?retryWrites=true&w=majority")
 
    # Database Name
    db = client["OneLink"]
    # Collection Name
    col = db["onelink"]

    if request.method == 'PATCH' :

        code = request.POST.get('code')
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        logo = request.FILES.get('logo')
        duration = request.POST.get('duration')
        sub_link = request.POST.get('sub_link')

        facebook = request.POST.get('facebook')
        facebooks_text = request.POST.get('facebooks_text')
        instagram = request.POST.get('instagram')
        instagrams_text = request.POST.get('instagrams_text')
        twitter = request.POST.get('twitter')
        twitters_text = request.POST.get('twitters_text')
        telegram = request.POST.get('telegram')
        telegrams_text = request.POST.get('telegrams_text')
        youtube = request.POST.get('youtube')
        youtubes_text = request.POST.get('youtubes_text')
        pinterest = request.POST.get('pinterest')
        pinterests_text = request.POST.get('pinterests_text')
        tiktok = request.POST.get('tiktok')
        tiktoks_text = request.POST.get('tiktoks_text')
        google = request.POST.get('google')
        google_text = request.POST.get('googleText')
        googles_text = request.POST.get('googles_text')

        website = request.POST.get('website')
        web_text = request.POST.get('webText')
        websites_text = request.POST.get('websites_text')
        phone = request.POST.get('phone')
        phone_text = request.POST.get('phoneText')
        phones_text = request.POST.get('phones_text')
        email = request.POST.get('email')
        email_text = request.POST.get('emailText')
        emails_text = request.POST.get('emails_text')

        location = request.POST.get('location')
        loc_text = request.POST.get('locText')
        locations_text = request.POST.get('locations_text')
        custom_link = request.POST.get('custom-link')
        custom_link_text = request.POST.get('custom-linkText')
        custom_links_text = request.POST.get('custom_links_text')

        type = request.POST.get('type')
        background_type = request.POST.get('bg-type')
        background_image = request.FILES.get('bg-image')
        background_color = request.POST.get('bg-color')
        font_color = request.POST.get('font-color')

        # update the data
        media = Media.objects.get(code=code)
        if logo != None :
            media.logo = logo
        if background_image != None :
            media.bg = background_image
        media.save()

        if name != '' :
            col.find_one_and_update({'code': code},{'$set': { "name" : name}})
        if desc != '' :
            col.find_one_and_update({'code': code},{'$set': { "desc" : desc}})
        if duration != '' :
            col.find_one_and_update({'code': code},{'$set': { "duration" : duration}})
        if facebook != '' :
            col.find_one_and_update({'code': code},{'$set': { "facebook" : facebook}})
        if facebooks_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "facebooks_text" : facebooks_text}})
        if instagram != '' :
            col.find_one_and_update({'code': code},{'$set': { "instagram" : instagram}})
        if instagrams_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "instagrams_text" : instagrams_text}})
        if twitter != '' :
            col.find_one_and_update({'code': code},{'$set': { "twitter" : twitter}})
        if twitters_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "twitters_text" : twitters_text}})
        if telegram != '' :
            col.find_one_and_update({'code': code},{'$set': { "telegram" : telegram}})
        if telegrams_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "telegrams_text" : telegrams_text}})
        if youtube != '' :
            col.find_one_and_update({'code': code},{'$set': { "youtube" : youtube}})
        if youtubes_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "youtubes_text" : youtubes_text}})
        if pinterest != '' :
            col.find_one_and_update({'code': code},{'$set': { "pinterest" : pinterest}})
        if pinterests_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "pinterests_text" : pinterests_text}})
        if tiktok != '' :
            col.find_one_and_update({'code': code},{'$set': { "tiktok" : tiktok}})
        if tiktoks_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "tiktoks_text" : tiktoks_text}})
        if google != '' :
            col.find_one_and_update({'code': code},{'$set': { "google" : google}})
        if google_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "google_text" : google_text}})
        if googles_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "googles_text" : googles_text}})
        if website != '' :
            col.find_one_and_update({'code': code},{'$set': { "website" : website}})
        if web_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "web_text" : web_text}})
        if websites_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "websites_text" : websites_text}})
        if phone != '' :
            col.find_one_and_update({'code': code},{'$set': { "phone" : phone}})
        if phone_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "phone_text" : phone_text}})
        if phones_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "phones_text" : phones_text}})
        if email != '' :
            col.find_one_and_update({'code': code},{'$set': { "email" : email}})
        if email_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "email_text" : email_text}})
        if emails_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "emails_text" : emails_text}})
        if location != '' :
            col.find_one_and_update({'code': code},{'$set': { "location" : location}})
        if loc_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "loc_text" : loc_text}})
        if locations_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "locations_text" : locations_text}})
        if custom_link != '' :
            col.find_one_and_update({'code': code},{'$set': { "custom_link" : custom_link}})
        if custom_link_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "custom_link_text" : custom_link_text}})
        if custom_links_text != '' :
            col.find_one_and_update({'code': code},{'$set': { "custom_links_text" : custom_links_text}})
        if type != '' :
            col.find_one_and_update({'code': code},{'$set': { "type" : type}})
        if background_type != '' :
            col.find_one_and_update({'code': code},{'$set': { "background_type" : background_type}})
        if background_image != '' :
            col.find_one_and_update({'code': code},{'$set': { "background_image" : 'Yes'}})
        if background_color != '' :
            col.find_one_and_update({'code': code},{'$set': { "background_color" : background_color}})
        if font_color != '' :
            col.find_one_and_update({'code': code},{'$set': { "font_color" : font_color}})
        if sub_link != '' :
            record = col.find_one({'sub_link': sub_link})
            if record is not None :
                return JsonResponse({
                    'result' : 'Sub Link already used.'
                })
            col.find_one_and_update({'code': code},{'$set': { "sub_link" : sub_link}})
        
        return JsonResponse({
            'result' : 'Patch successful.'
        })

    return JsonResponse({
        'result' : 'Patch failed.'
    })

@api_view(['DELETE'])
def delete (request) :

    client = pymongo.MongoClient("mongodb+srv://dbonelink:S7wRp1NZWxp2zsjz@onelink.gfjk5uq.mongodb.net/?retryWrites=true&w=majority")
 
    # Database Name
    db = client["OneLink"]
    # Collection Name
    col = db["onelink"]

    if request.method == 'DELETE' :

        code = request.POST.get('code')

        media = Media.objects.filter(code=code).all()
        media.delete()

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
    col = db["onelink"]

    record = col.find_one({'sub_link': subLink})
    if record is None :
        return render(request, '404.html')
        
    current_date = datetime.date.today()
    difference = (current_date - datetime.datetime.strptime(record.get('register_date'), '%Y-%m-%d').date()).days
    if int(difference) > int(record.get('duration')) :
        return render(request, '404.html')

    # check single or multiple
    if record.get('type') == 'multiple' :
        # get every attribute
        facebook, instagram, twitter, telegram, youtube, pinterest, tiktok, google, website, phone, email, location, custom_link = '' , '', '', '' , '', '', '', '', '', '', '', '', ''
        facebooks, instagrams, twitters, telegrams, youtubes, pinterests, tiktoks, googles, websites, phones, emails, locations, custom_links = [], [], [], [], [], [], [], [], [], [], [], [], []
        facebooks_text, instagrams_text, twitters_text, telegrams_text, youtubes_text, pinterests_text, tiktoks_text, googles_text, websites_text, phones_text, emails_text, locations_text, custom_links_text = [], [], [], [], [], [], [], [], [], [], [], [], []

        if '-' in record.get('facebook') :
            facebook = '#'
            facebooks = str(record.get('facebook')).split('-')
            facebooks_text = str(record.get('facebooks_text')).split('-')

        if '-' not in record.get('facebook') :
            facebook = record.get('facebook')
        
        if '-' in record.get('instagram') :
            instagram = '#'
            instagrams = str(record.get('instagram')).split('-')
            instagrams_text = str(record.get('instagrams_text')).split('-')

        if '-' not in record.get('instagram') :
            instagram = record.get('instagram')
        
        if '-' in record.get('twitter') :
            twitter = '#'
            twitters = str(record.get('twitter')).split('-')
            twitters_text = str(record.get('twitters_text')).split('-')

        if '-' not in record.get('twitter') :
            twitter = record.get('twitter')
        
        if '-' in record.get('telegram') :
            telegram = '#'
            telegrams = str(record.get('telegram')).split('-')
            telegrams_text = str(record.get('telegrams_text')).split('-')

        if '-' not in record.get('telegram') :
            telegram = record.get('telegram')
        
        if '-' in record.get('youtube') :
            youtube = '#'
            youtubes = str(record.get('youtube')).split('-')
            youtubes_text = str(record.get('youtubes_text')).split('-')

        if '-' not in record.get('youtube') :
            youtube = record.get('youtube')
        
        if '-' in record.get('pinterest') :
            pinterest = '#'
            pinterests = str(record.get('pinterest')).split('-')
            pinterests_text = str(record.get('pinterests_text')).split('-')

        if '-' not in record.get('pinterest') :
            pinterest = record.get('pinterest')
        
        if '-' in record.get('tiktok') :
            tiktok = '#'
            tiktoks = str(record.get('tiktok')).split('-')
            tiktoks_text = str(record.get('tiktoks_text')).split('-')

        if '-' not in record.get('tiktok') :
            tiktok = record.get('tiktok')
        
        if '-' in record.get('google') :
            google = '#'
            googles = str(record.get('google')).split('-')
            googles_text = str(record.get('googles_text')).split('-')

        if '-' not in record.get('google') :
            google = record.get('google')
        
        if '-' in record.get('website') :
            website = '#'
            websites = str(record.get('website')).split('-')
            websites_text = str(record.get('websites_text')).split('-')

        if '-' not in record.get('website') :
            website = record.get('website')
        
        if '-' in record.get('phone') :
            phone = '#'
            phones = str(record.get('phone')).split('-')
            phones_text = str(record.get('phones_text')).split('-')

        if '-' not in record.get('phone') :
            phone = 'tel:' + record.get('phone')
        
        if '-' in record.get('email') :
            email = '#'
            emails = str(record.get('email')).split('-')
            emails_text = str(record.get('emails_text')).split('-')

        if '-' not in record.get('email') :
            email = 'mailto:' + record.get('email')
        
        if '-' in record.get('location') :
            location = '#'
            locations = str(record.get('location')).split('-')
            locations_text = str(record.get('locations_text')).split('-')

        if '-' not in record.get('location') :
            location = record.get('location')
        
        if '-' in record.get('custom_link') :
            custom_link = '#'
            custom_links = str(record.get('custom_link')).split('-')
            custom_links_text = str(record.get('custom_links_text')).split('-')

        if '-' not in record.get('custom_link') :
            custom_link = record.get('custom_link')
        

        # check wheather the backgroud is image or color
        if record.get('background_type') == 'image' :
            #get the background
            if Media.objects.filter(code=record.get('code')).exists() :
                media = Media.objects.get(code=record.get('code'))

                return render(request, 'bgtemplate.html', {
                    'code' : record.get('code'),
                    'name' : record.get('name'),
                    'logo' : media.logo,
                    'desc' : record.get('desc'),
                    'facebook' : facebook,
                    'facebook_val' : zip(facebooks,facebooks_text),
                    'instagram' : instagram,
                    'instagram_val' : zip(instagrams,instagrams_text),
                    'twitter' : twitter,
                    'twitter_val' : zip(twitters,twitters_text),
                    'telegram' : telegram,
                    'telegram_val' : zip(telegrams,telegrams_text),
                    'youtube' : youtube,
                    'youtube_val' : zip(youtubes,youtubes_text),
                    'pinterest' : pinterest,
                    'pinterest_val' : zip(pinterests,pinterests_text),
                    'tiktok' : tiktok,
                    'tiktok_num' : zip(tiktoks,tiktoks_text),
                    'google' : google,
                    'googleText' : record.get('google_text'),
                    'google_val' : zip(googles,googles_text),
                    'website' : website,
                    'websiteText' : record.get('web_text'),
                    'website_val' : zip(websites,websites_text),
                    'phone' : phone,
                    'phoneText' : record.get('phone_text'),
                    'phone_val' : zip(phones,phones_text),
                    'email' : email,
                    'emailText' : record.get('email_text'),
                    'email_val' : zip(emails,emails_text),
                    'location' : location,
                    'locText' : record.get('loc_text'),
                    'location_val' : zip(locations,locations_text),
                    'customlink' : custom_link,
                    'customlinkText' : record.get('custom_link_text'),
                    'custom_link_val' : zip(custom_links,custom_links_text),
                    'backgroundImage' : media.bg,
                    'fontColor' : record.get('font_color')
                })

        if record.get('background_type') == 'color' :
            #get the logo only
            if Media.objects.filter(code=record.get('code')).exists() :
                media = Media.objects.get(code=record.get('code'))

                return render(request, 'colortemplate.html', {
                    'code' : record.get('code'),
                    'name' : record.get('name'),
                    'logo' : media.logo,
                    'desc' : record.get('desc'),
                    'facebook' : facebook,
                    'facebook_val' : zip(facebooks,facebooks_text),
                    'instagram' : instagram,
                    'instagram_val' : zip(instagrams,instagrams_text),
                    'twitter' : twitter,
                    'twitter_val' : zip(twitters,twitters_text),
                    'telegram' : telegram,
                    'telegram_val' : zip(telegrams,telegrams_text),
                    'youtube' : youtube,
                    'youtube_val' : zip(youtubes,youtubes_text),
                    'pinterest' : pinterest,
                    'pinterest_val' : zip(pinterests,pinterests_text),
                    'tiktok' : tiktok,
                    'tiktok_num' : zip(tiktoks,tiktoks_text),
                    'google' : google,
                    'googleText' : record.get('google_text'),
                    'google_val' : zip(googles,googles_text),
                    'website' : website,
                    'websiteText' : record.get('web_text'),
                    'website_val' : zip(websites,websites_text),
                    'phone' : phone,
                    'phoneText' : record.get('phone_text'),
                    'phone_val' : zip(phones,phones_text),
                    'email' : email,
                    'emailText' : record.get('email_text'),
                    'email_val' : zip(emails,emails_text),
                    'location' : location,
                    'locText' : record.get('loc_text'),
                    'location_val' : zip(locations,locations_text),
                    'customlink' : custom_link,
                    'customlinkText' : record.get('custom_link_text'),
                    'custom_link_val' : zip(custom_links,custom_links_text),
                    'backgroundColor' : record.get('background_color'),
                    'fontColor' : record.get('font_color')
                })

    
    if record.get('type') == 'single' :
        # check wheather the backgroud is image or color
        if record.get('background_type') == 'image' :
            #get the background
            if Media.objects.filter(code=record.get('code')).exists() :
                media = Media.objects.get(code=record.get('code'))

                return render(request, 'bgtemplate.html', {
                    'code' : record.get('code'),
                    'name' : record.get('name'),
                    'logo' : media.logo,
                    'desc' : record.get('desc'),
                    'facebook' : record.get('facebook'),
                    'instagram' : record.get('instagram'),
                    'twitter' : record.get('twitter'),
                    'telegram' : record.get('telegram'),
                    'youtube' : record.get('youtube'),
                    'pinterest' : record.get('pinterest'),
                    'tiktok' : record.get('tiktok'),
                    'google' : record.get('google'),
                    'googleText' : record.get('google_text'),
                    'website' : record.get('website'),
                    'websiteText' : record.get('web_text'),
                    'phone' : 'tel:' + record.get('phone'),
                    'phoneText' : record.get('phone_text'),
                    'email' : 'mailto:' + record.get('email'),
                    'emailText' : record.get('email_text'),
                    'location' : record.get('location'),
                    'locText' : record.get('loc_text'),
                    'customlink' : record.get('custom_link'),
                    'customlinkText' : record.get('custom_link_text'),
                    'backgroundImage' : media.bg,
                    'fontColor' : record.get('font_color')
                })

        else :
            #get the logo only
            if Media.objects.filter(code=record.get('code')).exists() :
                media = Media.objects.get(code=record.get('code'))

                return render(request, 'colortemplate.html', {
                    'code' : record.get('code'),
                    'name' : record.get('name'),
                    'logo' : media.logo,
                    'desc' : record.get('desc'),
                    'facebook' : record.get('facebook'),
                    'instagram' : record.get('instagram'),
                    'twitter' : record.get('twitter'),
                    'telegram' : record.get('telegram'),
                    'youtube' : record.get('youtube'),
                    'pinterest' : record.get('pinterest'),
                    'tiktok' : record.get('tiktok'),
                    'google' : record.get('google'),
                    'googleText' : record.get('google_text'),
                    'website' : record.get('website'),
                    'websiteText' : record.get('web_text'),
                    'phone' : 'tel:' + record.get('phone'),
                    'phoneText' : record.get('phone_text'),
                    'email' : 'mailto:' + record.get('email'),
                    'emailText' : record.get('email_text'),
                    'location' : record.get('location'),
                    'locText' : record.get('loc_text'),
                    'customlink' : record.get('custom_link'),
                    'customlinkText' : record.get('custom_link_text'),
                    'backgroundColor' : record.get('background_color'),
                    'fontColor' : record.get('font_color')
                })
    
    return render(request, '404.html')
