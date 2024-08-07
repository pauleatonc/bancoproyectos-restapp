# standard library
from datetime import timedelta, datetime
#
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
#
from applications.base.models import BaseModel
from applications.projects.models import Program
# apps de terceros
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from simple_history.models import HistoricalRecords


class InnovativeProjects(BaseModel):
    """
    Modelo para proyectos innovadores
    """
    title = models.CharField(max_length=23, verbose_name='Título (obligatorio)', unique=True, blank=True)
    description = models.TextField(validators=[MinLengthValidator(280, 'La descripción debe tener al menos 280 caracteres.')], blank=True)
    portada = ProcessedImageField(upload_to='projects', processors=[
        ResizeToFill(1200, 630)], format='WEBP', options={'quality': 60}, null=True,
                                  blank=True, verbose_name='Foto portada (obligatorio)')
    program = models.ForeignKey(Program, blank=True, null=True, verbose_name='Programa (obligatorio)', on_delete=models.SET_NULL)
    public = models.BooleanField(default=False)

    # request_sent debe cambiar a True si el proyecto es enviado a revisión. Debe cambiar nuevamente a False cuando evaluated sea True
    request_sent = models.BooleanField(default=False)

    # evaluated debe cambiar a True cuando el proyecto sea evaluado. Debe cambiar nuevamente a False si request_sent sea True
    evaluated = models.BooleanField(default=False)


    def fields_completed(self):
        # Valida que los campos obligatorios no estén en blanco
        return all([self.title, self.description, self.portada, self.program])

    @property
    def application_status(self):
        if not self.fields_completed():
            return "Incompleto"

        if self.evaluated:
            # Verificar si los objetos relacionados existen antes de acceder a ellos
            if ((hasattr(self, 'revision_section_one') and self.revision_section_one.approved_section_one) and
                    (hasattr(self, 'revision_section_two') and self.revision_section_two.approved_section_two)):

                # Comprueba si el campo 'public' es True
                if self.public:
                    return "Publicado"
                else:
                    return "Privado"

            else:
                return "Rechazado"

        else:
            if self.request_sent and self.fields_completed():
                return "Pendiente"
            else:
                return "Incompleto"

    def clean(self):
        # Validación personalizada
        if self.public and not self.fields_completed():
            raise ValidationError('El proyecto debe estar "Completo" para ser público.')

    def save(self, *args, **kwargs):
        self.clean()
        super(InnovativeProjects, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Proyecto Innovador'
        verbose_name_plural = 'Proyectos Innovadores'

    def __str__(self):
        return self.title


class InnovativeWebSource(models.Model):
    url = models.URLField()
    project = models.ForeignKey('InnovativeProjects', related_name='web_sources', on_delete=models.CASCADE)
    history = HistoricalRecords()


class InnovativeGalleryImage(models.Model):
    image = ProcessedImageField(
        upload_to='innovative_gallery_images',
        processors=[ResizeToFill(1200, 630)],
        format='WEBP',
        options={'quality': 60},
        null=True,
        blank=True
    )
    project = models.ForeignKey('InnovativeProjects', related_name='innovative_gallery_images', on_delete=models.CASCADE)
    history = HistoricalRecords()


class RevisionSectionOne(models.Model):
    """
    Campos para revisión y aprobación
    """
    approved_title = models.BooleanField(verbose_name='Error en el título', default=True)
    approved_description = models.BooleanField(verbose_name='Error en la descripción del proyecto', default=True)
    approved_program = models.BooleanField(verbose_name='Programa incorrecto', default=True)

    approved_section_one = models.BooleanField(default=False)

    project = models.OneToOneField('InnovativeProjects', related_name='revision_section_one',  on_delete=models.CASCADE)
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if all((not self.approved_title, not self.approved_description, not self.approved_program)):
            if not self.approved_section_one:
                raise ValueError('El campo approved_section_one debe ser True si todos los otros campos son False')
        super().save(*args, **kwargs)

    def clean(self):
        if all((not self.approved_title, not self.approved_description, not self.approved_program)):
            if not self.approved_section_one:
                raise ValidationError('El campo approved_section_one debe ser True si todos los otros campos son False')


class RevisionSectionTwo(models.Model):
    """
    Campos para revisión y aprobación
    """
    approved_portada = models.BooleanField(verbose_name='Foto de portada con problemas', default=True)
    approved_gallery = models.BooleanField(verbose_name='Fotos de la galería con problemas', default=True)
    approved_web_source = models.BooleanField(verbose_name='Error en la fuente o enlace', default=True)

    approved_section_two = models.BooleanField(default=False)

    project = models.OneToOneField('InnovativeProjects', related_name='revision_section_two', on_delete=models.CASCADE)
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if all((not self.approved_portada, not self.approved_gallery, not self.approved_web_source)):
            if not self.approved_section_two:
                raise ValueError('El campo approved_section_two debe ser True si todos los otros campos son False')
        super().save(*args, **kwargs)

    def clean(self):
        if all((not self.approved_portada, not self.approved_gallery, not self.approved_web_source)):
            if not self.approved_section_two:
                raise ValidationError('El campo approved_section_two debe ser True si todos los otros campos son False')
