from . import models
from modeltranslation.translator import TranslationOptions, register

@register(models.Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

    
@register(models.News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)