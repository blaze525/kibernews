from django.contrib import admin
from . import models
from modeltranslation.admin import TranslationAdmin


@admin.register(models.Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name',)
    
    group_fieldsets = True
    
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js',
        'https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    
    
admin.site.register(models.News)
admin.site.register(models.Banner)