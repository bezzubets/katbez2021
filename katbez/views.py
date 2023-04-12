from django.shortcuts import render
from .models import TitlePic,TitleGallery,Pics
from django.views import generic


def index(request):
    titlepic = TitlePic.objects.all()
    context ={
        'titlepic':titlepic,
    }


    return render(request, 'index.html', context)

def bio(request):
    titlepic = TitlePic.objects.all()
    context ={
        'titlepic':titlepic,
    }


    return render(request, 'bio.html', context)

def contacts(request):
    titlepic = TitlePic.objects.all()
    context ={
        'titlepic':titlepic,
    }


    return render(request, 'contacts.html', context)

def galleries(request):
    titlepic = TitlePic.objects.all()
    tg = TitleGallery.objects.all()
    context ={
        'titlepic':titlepic,
        'tg':tg,
    }


    return render(request, 'galleries.html', context)

def get_gallery(request, gallery_pk):
    tg = TitleGallery.objects.get(pk = gallery_pk)
    tgs = TitleGallery.objects.all().filter(pk = gallery_pk)
    pics = Pics.objects.filter(pk=gallery_pk)
    context = {'tg': tg,'tgs': tgs, 'pics':pics,  }
    return render(request, 'gallery.html', context=context)
