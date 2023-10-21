from modeltranslation.translator import translator, TranslationOptions,register
from .models import Product,Color,Review,Category


class ProductTranslationOptions(TranslationOptions):
    fields = ('description',)
translator.register(Product,ProductTranslationOptions)

class ColorTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(Color,ColorTranslationOptions)

class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)
translator.register(Review,ReviewTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
translator.register(Category,CategoryTranslationOptions)