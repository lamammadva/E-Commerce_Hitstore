from modeltranslation.translator import translator, TranslationOptions,register
from .models import Blogs,Category


class BlogsTranslationOptions(TranslationOptions):
    fields = ('description','title',)
translator.register(Blogs,BlogsTranslationOptions)

# class CommentTranslationOptions(TranslationOptions):
#     fields = ('comment',)
# translator.register(Comments,CommentTranslationOptions)

