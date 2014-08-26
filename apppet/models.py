from tastypie.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

class Status(models.Model):
    status = models.CharField(max_length=100)
class Type(models.Model):
    type = models.CharField(max_length=100)
class Cao_raca(models.Model):
    raca = models.CharField(max_length=100)
class Cor(models.Model):
    cor = models.CharField(max_length=100)
class Cor_olhos(models.Model):
    cor_olhos = models.CharField(max_length=255)
class Sexo(models.Model):
    sexo = models.CharField(max_length=255)
class Peso(models.Model):
    peso = models.IntegerField()
class Register(models.Model):
    nome = models.CharField(max_length=60)
    sexo = models.CharField(max_length=10)
    telefone = models.CharField(max_length=10)
    endereco = models.CharField(max_length=70)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=2)
    cep = models.IntegerField()
    email = models.CharField(max_length=60)
    senha = models.CharField(max_length=12)
class Animal(models.Model):
    type = models.ForeignKey(Type)
    raca = models.ForeignKey(Cao_raca)
    status = models.ForeignKey(Status)
    sexo = models.ForeignKey(Sexo)
    cor_olhos = models.ForeignKey(Cor_olhos)
    peso = models.ForeignKey(Peso)
    coleira = models.CharField(max_length=10)
    porte = models.CharField(max_length=10)
    mancha = models.CharField(max_length=60)
    cor = models.CharField(max_length=60)
    orelha = models.CharField(max_length=10)
    orelha_ciada = models.CharField(max_length=10)
    orelha_ciada_lado = models.CharField(max_length=10)
    rabo = models.CharField(max_length=10)
    cicatriz = models.CharField(max_length=10)
    local_cicatriz = models.CharField(max_length=60)
    falta_dente = models.CharField(max_length=10)
    mancha_lingua = models.CharField(max_length=10)
    temperamento = models.CharField(max_length=20)
    microchip = models.CharField(max_length=10)
    microchip_id = models.CharField(max_length=60)
    nome = models.CharField(max_length=60)
    membro_amputado = models.CharField(max_length=10)
    membdro_amputado_id = models.CharField(max_length=60)
    num_mama = models.CharField(max_length=10)
