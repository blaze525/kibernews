from . import models
from modeltranslation.translator import TranslationOptions, register

@register(models.Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
