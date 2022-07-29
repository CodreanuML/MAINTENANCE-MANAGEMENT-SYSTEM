from django.contrib import admin
from .models import Zona,Asset,SubAsset,AvarieAsset
# Register your models here.
admin.site.register(Zona)
admin.site.register(Asset)
admin.site.register(SubAsset)
admin.site.register(AvarieAsset)
