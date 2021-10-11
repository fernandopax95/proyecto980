from django.contrib import admin
from .models import Mascota, Vacuna
# Register your models here.

admin.site.register(Mascota)
admin.site.register(Vacuna)

class MascotaAdmin(admin.ModelAdmin):
    list_display= ('nombre','folio')

class MascotaInstanceAdmin(admin.ModelAdmin):
    list_filter = ('nombre','folio')