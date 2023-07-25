from django.db import models

class Propietario(models.Model):
    cedula = models.CharField(max_length=30) 
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
     
    def _str_(self):
        return "%s %s %s %s" % (self.nombre,
                                self.apellido,
                                self.cedula)  

class Edificio(models.Model):
    opciones_tipo_Edificio = (
        ('Residencial', 'Residencial'),
        ('Negocio', 'Negocio'),
        ('Público', 'Público'),
    )

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, \
                            choices=opciones_tipo_Edificio)

    def _str_(self):
        return "%s %s %s %s" % (self.nombre,
                                self.direccion,
                                self.ciudad,
                                self.tipo)

class Departamento(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
                                 related_name="PropietarioDepar")

    costo = models.FloatField()
    num_cuartos = models.IntegerField()

    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
                                 related_name="Departamentos")

    def _str_(self):
        return "%s %s %d %s" % (self.propietario,
                                self.costo,
                                self.num_cuartos,
                                self.edificio)