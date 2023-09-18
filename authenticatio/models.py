from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)
    
    def __str__(self):
        return f'{self.usuario.first_name} {self.usuario.last_name}' 
    def clean(self) :
        return super().clean()