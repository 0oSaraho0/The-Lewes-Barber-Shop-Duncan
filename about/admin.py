from django.contrib import admin
from .models import About, Artist

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'about',
        'image',
    )
    list_filter = ('about',)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'artist',
        'image',
        'website',
        'about',
    )
    list_filter = ('about',)
