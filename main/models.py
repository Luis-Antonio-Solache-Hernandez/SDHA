from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Etiqueta(models.Model):
    etiqueta = models.CharField(max_length=15, unique=True)

    def __unicode__(self):
        return '%s' % self.lista

    class Meta:
        ordering = ['-etiqueta']


class Perfil(models.Model):
    ESTADO_CHOICES = (
        ('Solter@', 'Solter@'),
        ('Casad@', 'Casad@'),
        ('Union Libre', 'Union Libre'),
        ('Separad@', 'Separad@'),
        ('Divorciad@', 'Divorciad@'),
        ('Viud@', 'Viud@'),
    )
    folio = models.CharField(max_length=5, unique=True)
    user = models.OneToOneField(User)
    nombre = models.CharField(max_length=60, unique=True)
    foto = models.FileField(upload_to="imagen", blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    telefono1 = models.CharField(max_length=15)
    telefono2 = models.CharField(max_length=15, blank=True, null=True)
    telefono3 = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    cumpleanios = models.DateField()
    estadocivil = models.CharField(max_length=11, choices=ESTADO_CHOICES)
    observacionesp = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        permissions = (
        # Permission identifier
        ("perm_secre", "permsecre"),
        )

    def __unicode__(self):
        return '%s' % self.nombre


def get_profile(user):
    if not hasattr(user, '_profile_cache'):
        profile, created = Perfil.objects.get_or_create(user=user, nombre=user.username, folio=user.id, cumpleanios=datetime.today())
        user._profile_cache = profile
    return user._profile_cache
User.get_profile = get_profile


class Lista(models.Model):
    nombre = models.CharField(max_length=15, unique=True)
    persona = models.ManyToManyField(Perfil, blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.nombre

    class Meta:
        ordering = ['-nombre']


#class Entrevista_Inicial(models.Model)


class Evento(models.Model):
    fecha = models.DateField()
    nombre = models.CharField(max_length=30)
    duracion = models.CharField(max_length=15)
    lugar = models.CharField(max_length=15)
    costo = models.DecimalField(max_digits=4, decimal_places=2)
    descripcion = models.TextField()
    observaciones = models.TextField()

    def __unicode__(self):
        return '%s' % self.nombre


class Sede(models.Model):
    lugar = models.CharField(max_length=20)

    def __unicode__(self):
        return '%s' % self.lugar


class Consulta(models.Model):
    fecha_hora = models.DateTimeField(unique=True)
    lugar = models.ForeignKey(Sede, verbose_name="Campus Sede")
    tpx = models.ForeignKey(Perfil, related_name="paciente titular", verbose_name="Titular Consulta")
    px = models.ManyToManyField(Perfil, blank=True, null=True, verbose_name="Asisten")
    consultor = models.ForeignKey(Perfil, related_name="consultor", blank=True, null=True)  # checar validaciion
    costo = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    evolucion = models.CharField(max_length=200, blank=True, null=True)
    observaciones = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return 'Consulta solicitada por %s en %s' % (self.px, self.fecha_hora,)


class Producto(models.Model):
    TIPO_CHOICES = (
            ('Libro', 'Libro'),
            ('CD', 'CD'),
            ('Manual', 'Manual'),
            ('Diploamado', 'Diploamado'),
            ('Conferencia', 'Conferencia'),
            ('Seminario', 'Seminario'),
            ('Libreto', 'Libreto'),
            ('Otros Servicios', 'Otros Servicios'),
    )
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=15)
    existencia = models.IntegerField()
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    imagen = models.FileField(upload_to="imagen")
    descripcion = models.CharField(max_length=100)
    tema = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s' % self.nombre


class List(models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()
    lugar = models.ForeignKey(Sede)
    etiqueta = models.ManyToManyField(Etiqueta)
    estado = models.CharField(max_length=20)
    observacion = models.CharField(max_length=75)
    titular = models.ForeignKey(Perfil)
    concurrencia = models.IntegerField()

    def Etiquetas(self):
        datos = self.etiqueta.all()
        tam = len(datos)
        etiquetas = ""
        for dato in datos:
            tam = tam - 1
            etiquetas = etiquetas + '%s' % dato.etiqueta
            if tam > 0:
                etiquetas = etiquetas + ', '
        return etiquetas

    def __unicode__(self):
        return '%s' % self.nombre


class TipoSem(models.Model):
    tipo = models.CharField(max_length=20)

    def __unicode__(self):
        return '%s' % self.tipo


class SemiDip(models.Model):
    nombre = models.CharField(max_length=30)
    lista = models.ForeignKey(List)
    tipo = models.ForeignKey(TipoSem)
    descripcion = models.CharField(max_length=50)
    horarios = models.CharField(max_length=40)
    info_evento = models.CharField(max_length=150)
    temas = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    libro = models.ForeignKey(Producto)

    def __unicode__(self):
        return '%s' % self.nombre


class BibliE(models.Model):
    expositor = models.ForeignKey(Perfil)
    tema = models.CharField(max_length=50)
    fecha = models.DateField()
    observaciones = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % self.tema


class Adeudo(models.Model):
    usuario = models.ForeignKey(Perfil)
    producto = models.ForeignKey(Producto)
    monto = models.DecimalField(max_digits=4, decimal_places=2)
    importe = models.DecimalField(max_digits=4, decimal_places=2)
    activo = models.BooleanField()

    def __unicode__(self):
        return 'Adeudo de %s' % self.usuario.user.username


class Abono(models.Model):
    adeudo = models.ForeignKey(Adeudo)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=4, decimal_places=2)

    def __unicode__(self):
        return 'Abono de %s' % self.adeudo.usuario.user.username
