from django.contrib import admin
from .models import Dispositivo
from .models import Usuario
from .models import Comuna
from .models import Provincia
from .models import Region
from .models import Propiedad
from .models import Sectores
from .models import TipoSector
from .models import TipoDispositivo
from .models import HorarioUso

# Register your models here.
admin.site.register(Dispositivo)
admin.site.register(Usuario)
admin.site.register(Comuna)
admin.site.register(Provincia)
admin.site.register(Region)
admin.site.register(Propiedad)
admin.site.register(Sectores)
admin.site.register(TipoSector)
admin.site.register(TipoDispositivo)
admin.site.register(HorarioUso)
