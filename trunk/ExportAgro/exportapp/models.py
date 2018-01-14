from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
# Create your models here.

class pais (models.Model):
    nombre_pais=models.CharField(max_length=60)
    def __str__(self):
        return self.nombre_pais

class mes(models.Model):
    nombre_mes=models.CharField(max_length=15)
    def __str__(self):
        return self.nombre_mes
 
class tipo_producto(models.Model):
    nombre_tipo=models.CharField(max_length=80)
    def __str__(self):
        return self.nombre_tipo
   
class producto(models.Model):
    codigo_arancelario=models.CharField(max_length=8,primary_key=True)
    nombre_producto=models.CharField(max_length=200)
    procesado=models.BooleanField(default=False)
    tipo_producto=models.ForeignKey(tipo_producto)
    def __str__(self):
        if self.procesado:
            return "Materia prima: "+self.tipo_producto.nombre_tipo+" ,nombre de producto: "+self.nombre_producto+" ,es procesado"
        else:
            return "Materia prima: "+ self.tipo_producto.nombre_tipo+" ,nombre de producto: "+self.nombre_producto+" ,no procesado"

class temporada(models.Model):
    numero_mes=models.ForeignKey(mes)
    anio=models.IntegerField()
    def __str__(self):
        return str(self.anio)+" mes : "+self.numero_mes.nombre_mes
  


class informacion_exportacion(models.Model):
   
    codigo_temporada=models.ForeignKey(temporada)
    costo_mercancia=models.DecimalField(max_digits=20,decimal_places=2)
    peso_kilogramos=models.DecimalField(max_digits=20,decimal_places=2)
    codigo_pais=models.ForeignKey(pais)
    codigo_producto=models.ForeignKey(producto)
    def __str__(self):
        return self.codigo_pais.nombre_pais+" exportacion de : "+self.codigo_producto.nombre_producto+" valores: $"+str(self.costo_mercancia)+" KG: "+str(self.peso_kilogramos)
    
class formula(models.Model):
    coeficiente=models.IntegerField()
    def __str__(self):
        return str(self.coeficiente)