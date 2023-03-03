from django.db import models

# Create your models here.
class Composition(models.Model):
    composit = models.CharField(max_length=200)
    def __str__(self):
        return self.composit
    class Meta:
        verbose_name_plural = "Компоненты"
class Diseases(models.Model):
    diseases = models.CharField(max_length=200)
    def __str__(self):
        return self.diseases
    class Meta:
        verbose_name_plural = "Болезни"
class Pills(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    diseases = models.ManyToManyField(Diseases)
    composition = models.ManyToManyField(Composition)
    used = models.TextField()
    effect = models.TextField()
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Лекарства"

