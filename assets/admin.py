from django.contrib import admin
from assets.models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('slug','title','creator')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Item, ItemAdmin)
