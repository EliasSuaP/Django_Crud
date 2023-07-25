from django.contrib import admin
from .models import Album, Artist, Customer, Employee, Genre, Invoice, Invoiceline, Mediatype, Playlist, Playlisttrack, Track

# Register your models here.
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Genre)
admin.site.register(Invoice)
admin.site.register(Invoiceline)
admin.site.register(Mediatype)
admin.site.register(Playlist)
admin.site.register(Playlisttrack)
admin.site.register(Track)