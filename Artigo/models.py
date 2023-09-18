from django.db import models

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from authenticatio.models import Perfil

class CategoriaArtigos(models.Model):
    nome = models.CharField(max_length=255)
    class Meta:
        ordering = ["nome"]
    
    def __str__(self):
        return self.nome
    
    
    
class Artigo(models.Model):
    Titulo = models.CharField(max_length=255)
    sinopse =  models.TextField(blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    envio_date = models.DateTimeField(default=timezone.now,editable=True)
    categoria = models.ForeignKey(CategoriaArtigos,on_delete=models.SET_NULL,null=True,blank=True)
    
    Usuario_id = models.ForeignKey(Perfil,on_delete=models.SET_NULL,null=True,blank=True)
    
    
    mostra = models.BooleanField(default=True)
    Capa = models.ImageField(blank=True,upload_to='fotos/%y/%m/%d/')
    pdf = models.FileField(upload_to='Artigos/%y/%m/%d/', blank=True)
    def __str__(self):
        return self.Titulo