from django.contrib import admin
from .models import Mashina, HaydovchilikGuvohnomasi

@admin.register(Mashina)
class MashinaAdmin(admin.ModelAdmin):
    list_display = ('turi', 'modeli', 'rangi', 'yili', 'davlat_raqami')
    search_fields = ('modeli', 'kuzov_raqami', 'davlat_raqami')
    list_filter = ('rangi', 'yili')

@admin.register(HaydovchilikGuvohnomasi)
class HaydovchilikGuvohnomasiAdmin(admin.ModelAdmin):
    list_display = ('ismi', 'familyasi', 'categoriyasi', 'guvohnoma_raqami')
    search_fields = ('ismi', 'familyasi', 'guvohnoma_raqami')
    list_filter = ('categoriyasi', 'amal_qilish_muddati')
