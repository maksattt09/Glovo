from .models import (Category, Store, Address, StoreMenu, Product, Order, Review)
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = ('store_name', 'description', 'owner')


@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ('address_name',)


@register(StoreMenu)
class StoreMenuTranslationOptions(TranslationOptions):
    fields = ('menu_name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'product_description')


@register(Order)
class OrderTranslationOptions(TranslationOptions):
    fields = ('delivery_address',)


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('text',)