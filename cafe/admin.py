from django.contrib import admin
from .models import Entrega, Productor, CentroAcopio, Bodega

# Register your models here.
admin.site.register(Productor)
admin.site.register(CentroAcopio)
admin.site.register(Entrega)
admin.site.register(Bodega)
