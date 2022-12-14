from django.contrib import admin

from. import models

class rizal(admin.ModelAdmin):
    list_display = ['Nama', 'NPM','Tanggal_lahir','Kode_pos']
    search_fields = ['Nama', 'NPM','Tanggal_lahir','Kode_pos']
    list_filter = ['Prodi']
    list_per_page = 2
class hj(admin.ModelAdmin):
    list_display = ['Nama', 'NPM', 'Judul_skripsi', 'Abstrak','Pembimbing']
    search_fields = ['Nama','Judul_skripsi','NPM']
    list_filter = ['Kode_skripsi']
    list_per_page = 4
class yk(admin.ModelAdmin):
    list_display = ['NAMA', 'Kode_matakuliah', 'Nilai_angka', 'Nilai_huruf']
    search_fields = ['Kode_matakuliah']
    list_filter = ['Nilai_angka', 'Nilai_huruf']
    list_per_page = 4

admin.site.register(models.mhs,rizal)
admin.site.register(models.skripsi,hj)
admin.site.register(models.th,yk)