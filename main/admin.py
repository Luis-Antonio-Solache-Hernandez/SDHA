from django.contrib import admin
from main.models import Etiqueta, Perfil, Evento, Sede, Consulta, Producto, List, TipoSem, SemiDip, BibliE, Adeudo, Abono, Lista


class EtiquetaInline(admin.TabularInline):
    model = List.etiqueta.through


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'telefono1', 'telefono2', 'telefono3', 'direccion', 'cumpleanios', 'estadocivil', 'observacionesp', 'foto', 'folio',)


class ListaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('etiqueta',)


class EventoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'nombre', 'duracion', 'lugar', 'costo', 'descripcion', 'observaciones', )


class SedeAdmin(admin.ModelAdmin):
    list_display = ('lugar',)


class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('fecha_hora', 'lugar', 'tpx', 'consultor', 'costo', 'evolucion', 'observaciones')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'existencia', 'tipo', 'precio', 'imagen', 'descripcion', 'tema',)


class ListAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'lugar', 'estado', 'observacion', 'titular', 'concurrencia', 'Etiquetas')
    inlines = [
        EtiquetaInline,
    ]


class TipoSemAdmin(admin.ModelAdmin):
    list_display = ('tipo',)


class SemiDipAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'lista', 'tipo', 'descripcion', 'horarios', 'info_evento', 'temas', 'fecha_inicio', 'fecha_fin', 'libro',)


class BibliEAdmin(admin.ModelAdmin):
    list_display = ('expositor', 'tema', 'fecha', 'observaciones',)


class AdeudoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'producto', 'monto', 'importe', 'activo',)


class AbonoAdmin(admin.ModelAdmin):
    list_display = ('adeudo', 'fecha', 'monto',)

admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Etiqueta, EtiquetaAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Sede, SedeAdmin)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(Lista, ListaAdmin)
admin.site.register(TipoSem, TipoSemAdmin)
admin.site.register(SemiDip, SemiDipAdmin)
admin.site.register(BibliE, BibliEAdmin)
admin.site.register(Adeudo, AdeudoAdmin)
admin.site.register(Abono, AbonoAdmin)
