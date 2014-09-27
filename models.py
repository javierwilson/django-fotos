from django.db import models
from sorl.thumbnail import ImageField
#from taggit.managers import TaggableManager

class Serie(models.Model):
    publicado = models.BooleanField(default=True)
    serie = models.CharField(max_length=100)
    texto = models.TextField(null=True, blank=True)
    class Meta:
        ordering = ['serie']
    def __unicode__(self):
        return self.serie

class Galeria(models.Model):
    galeria = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    texto = models.TextField(null=True, blank=True)
    class Meta:
        ordering = ['galeria']
    def __unicode__(self):
        return self.galeria

class Expo(models.Model):
    publicado = models.BooleanField(default=True)
    expo = models.CharField(max_length=100)
    galeria = models.ForeignKey(Galeria)
    fecha = models.DateField()
    texto = models.TextField(null=True, blank=True)
    imagen = ImageField(upload_to='expo', null=True, blank=True)
    class Meta:
        ordering = ['-fecha','expo']
    def __unicode__(self):
        return self.expo

class Foto(models.Model):
    publicado = models.BooleanField(default=True)
    foto = models.CharField(max_length=200)
    serie = models.ForeignKey(Serie, null=True)
    expo = models.ManyToManyField(Expo, null=True, blank=True)
    imagen = ImageField(upload_to='fotos')
    #tags = TaggableManager(blank=True)
    class Meta:
        ordering = ['foto']
    def __unicode__(self):
        return self.foto

