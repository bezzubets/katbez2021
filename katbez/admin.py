from django.contrib import admin
from.models import TitleGallery, TitlePic, Pics

class PicsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desription', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12',
        'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20']
    list_filter = ['id', 'title', ]

admin.site.register(TitleGallery)
admin.site.register(TitlePic)
admin.site.register(Pics)


