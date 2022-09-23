from django.db import models
# import richtextfield
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(verbose_name="Contenido")
    slug = models.CharField(max_length=150, unique=True, verbose_name="URL")
    order = models.IntegerField(default=0, verbose_name="Orden")
    visible = models.BooleanField(verbose_name="¿Visible?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name="Página"
        verbose_name_plural="Páginas"
        
    def __str__(self):
        return self.title