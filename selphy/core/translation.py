from modeltranslation.translator import translator, TranslationOptions,register
from .models import Core

class CoreTranslationOptions(TranslationOptions):
    fields = ('description',)
translator.register(Core,CoreTranslationOptions)
