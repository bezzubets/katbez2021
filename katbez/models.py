from django.db import models

class TitleGallery(models.Model):
    gallery = models.CharField(max_length=100)
    def __str__(self):
        return self.gallery


class Pics(models.Model):
    title = models.ForeignKey(TitleGallery,on_delete=models.CASCADE)
    desription = models.CharField(max_length=100,blank=True)
    p1 = models.ImageField(upload_to='static/pics/',blank=True)
    p2 = models.ImageField(upload_to='static/pics/',blank=True)
    p3 = models.ImageField(upload_to='static/pics/',blank=True)
    p4 = models.ImageField(upload_to='static/pics/',blank=True)
    p5 = models.ImageField(upload_to='static/pics/',blank=True)
    p6 = models.ImageField(upload_to='static/pics/',blank=True)
    p7 = models.ImageField(upload_to='static/pics/',blank=True)
    p8 = models.ImageField(upload_to='static/pics/',blank=True)
    p9 = models.ImageField(upload_to='static/pics/',blank=True)
    p10 = models.ImageField(upload_to='static/pics/',blank=True)
    p11 = models.ImageField(upload_to='static/pics/',blank=True)
    p12 = models.ImageField(upload_to='static/pics/',blank=True)


class TitlePic(models.Model):
    titlepic = models.ImageField(upload_to='static/titlepic/')

