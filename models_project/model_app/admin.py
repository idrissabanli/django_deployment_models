from django.contrib import admin
from .models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject')

admin.site.register(Video)
admin.site.register(Blogger)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = (('title', 'author'), ('price', 'page_count', 'cover_image', 'description'), 'categories')
    list_display = ('title', 'author')
    search_fields = ('title',)
    list_filter = ('author',)
    fieldsets = (
        ('Information', {
            'fields':('title', 'price')
        }),
        ('Other', {
            'fields':('author', 'page_count')
        }), 
    )
    
# admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Contact, ContactAdmin)