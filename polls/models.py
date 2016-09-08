from django.db import models

class Paciente(models.Model):
    nombre_text = models.CharField(('Nombre'),max_length=200)
    apellido_text = models.CharField(('Apellido'),max_length=200)
    cedula_text = models.CharField(('Cedula'),max_length=8)
    nacimiento_date = models.DateField('Fecha de nacimiento')
    telefono_text = models.CharField(('Telefono'),max_length=200, null=True, blank=True)
    direccion_text = models.CharField(('Direccion'),max_length=200, null=True, blank=True)
    correo_text = models.CharField(('Correo electronico'),max_length=200, null=True, blank=True)
    mutualista_text = models.CharField(('Mutualista'),max_length=200, null=True, blank=True)
    antecedentes_familiares_text = models.TextField(('Antecedentes Familiares'),null=True, blank=True)
    antecedentes_personales_text = models.TextField(('Antecedentes Personales'),null=True, blank=True)
    otros_text = models.TextField(('Otros'),null=True, blank=True)
    historial_text = models.TextField(('Historial'),null=True, blank=True)

    def __str__(self):
        """
        Este metodo le permite a muchas secciones de django convertir tu objeto en un string legible distinto de Paciente Object
        """
        return self.nombre_text + ' '  + self.apellido_text

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class Receta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_receta_text = models.DateField('Fecha receta', null=True, blank=True)
    historia_clinica_text = models.TextField(('Historia Clinica'),null=True, blank=True)
    lejos_od_text = models.TextField(('Lejos OD'),null=True, blank=True)
    lejos_oi_text = models.TextField(('Lejos OI'),null=True, blank=True)
    cerca_od_text = models.TextField(('Cerca OD'),null=True, blank=True)
    cerca_oi_text = models.TextField(('Cerca OI'),null=True, blank=True)
    add_text = models.TextField(('ADD'),null=True, blank=True)

    def __str__(self):
        return str(self.paciente) + ' : ' + str(self.fecha_receta_text)

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'

class Examen(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_examen_text = models.DateField('Fecha examen', null=True, blank=True)
    motivo_text = models.CharField(('Motivo'),max_length=200, null=True, blank=True)
    tension_ocular_text = models.CharField(('Tension ocular'),max_length=200, null=True, blank=True)
    examen_ocular_text = models.TextField(('Examen ocular'),null=True, blank=True)
    examen_compl_text = models.CharField(('Examenes complementarios'),max_length=200, null=True, blank=True)
    tratamiento_text = models.TextField(('Tratamiento'),null=True, blank=True)
    od_sin_lentes_text = models.CharField(('Agudza Visual sin lentes ojo derecho'),max_length=200, null=True, blank=True)
    oi_sin_lentes_text = models.CharField(('Agudza Visual sin lentes ojo izquierdo'),max_length=200, null=True, blank=True)
    od_con_lentes_text = models.CharField(('Agudza Visual con lentes ojo derecho'),max_length=200, null=True, blank=True)
    oi_con_lentes_text = models.CharField(('Agudza Visual con lentes ojo izquierdo'),max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.paciente) + ' : ' + str(self.fecha_examen_text)

    class Meta:
        verbose_name = 'Examen'
        verbose_name_plural = 'Examenes'
