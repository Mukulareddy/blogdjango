from django.contrib import admin
from entry.models import Entry, Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)
admin.site.register(Category, CategoryAdmin)

class EntryAdmin(admin.ModelAdmin):

	list_display =('id', 'title', 'text')

admin.site.register(Entry, EntryAdmin)