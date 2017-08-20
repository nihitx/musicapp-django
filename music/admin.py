from django.contrib import admin
from .models import Album, Song
#register the album so the admin dashboard can seeit
admin.site.register(Album)
admin.site.register(Song)
