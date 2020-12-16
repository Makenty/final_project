from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Название', max_length=250)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Parents(models.Model):
    mather = models.CharField ('mam', max_length=11)
    father = models.CharField ('pap', max_length=11)




class Madi(models.Model):
    name = models.CharField('name', max_length=11)
    parents = models.ForeignKey('Parents', on_delete=models.SET_NULL, null=True)
