from django.contrib import admin

from .models import Paciente
from .models import Examen
from .models import Receta


#class ExamenInline(admin.TabularInline):
#    model = Examen
#    extra = 1

class ExamenInline(admin.StackedInline):
    model = Examen
    extra = 1


class RecetaInline(admin.StackedInline):
    model = Receta
    extra = 1


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nombre_text', 'apellido_text', 'cedula_text']  # lista de campos del objeto que voy a mostrar en el listview del objeto en el admin. Primer campo tiene link al detalle, se puede atravesar relaciones simples
    search_fields = ['nombre_text', 'apellido_text', 'cedula_text']  # Lista de campos hacia los cuales se puede buscar, admite relaciones simples
    list_filter = ['nacimiento_date']  # Lista de campos para los que aparece un control especifico de filtrado en el admin.
    inlines = [ExamenInline, RecetaInline]


admin.site.register(Examen)
admin.site.register(Receta)
