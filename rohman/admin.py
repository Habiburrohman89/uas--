from django.contrib import admin

from .import models

class ed(admin.ModelAdmin):
    list_display = ['NAMA','TETALA','ALAMAT']
    search_fields = ['NAMA']
    list_filter = ['KODEPOS']
    list_per_page = 2



admin.site.register(models.editor,ed)
