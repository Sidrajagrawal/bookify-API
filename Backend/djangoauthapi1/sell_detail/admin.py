from django.contrib import admin
from sell_detail.models import SellDetail, BookPhoto

@admin.register(SellDetail)
class SellDetailAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'book_author', 'book_quantity', 'book_expected_price', 'created_at', 'updated_at', 'deleted_at')
    search_fields = ('book_title', 'book_author')
    list_filter = ('created_at', 'updated_at', 'deleted_at')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')  

@admin.register(BookPhoto)
class BookPhotoAdmin(admin.ModelAdmin):
    list_display = ('sell_detail', 'created_at')
    search_fields = ('sell_detail__book_title',)
    list_filter = ('created_at',)