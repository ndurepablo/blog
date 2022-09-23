from django.contrib import admin
from .models import Page

# Custom list display for Page model
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at')
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(Page, PageAdmin) 
    
# Change panel title:
admin.site.site_header = "Gestión de Páginas"
admin.site.site_title = "Gestión de Páginas"
admin.site.index_title = "Panel de Páginas"
