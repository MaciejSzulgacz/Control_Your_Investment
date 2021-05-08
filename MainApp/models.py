from django.db import models


class Person(models.Model):
    full_name = models.CharField(max_length=64, unique=True)
    position = models.CharField(max_length=64)

    def __str__(self):
        return self.full_name


class Machine(models.Model):
    machine_model = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.machine_model


class Task(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateField()
    finish_date = models.DateField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    machine = models.ManyToManyField(Machine, related_name='machine')

    def __str__(self):
        return self.name


class Subcontractor(models.Model):
    INDUSTRY_CHOICES = (
        (1, 'Construction Works'),
        (2, 'Bridge Works'),
        (3, 'Road Works'),
        (4, 'Track Works'),
        (5, 'Sanitary Works'),
        (6, 'Telecommunication Works'),
        (7, 'Electric Works'),
    )
    name = models.CharField(max_length=64, unique=True)
    industry = models.IntegerField(choices=INDUSTRY_CHOICES)
    tasks = models.ManyToManyField(Task)


class ConstructionSide(models.Model):
    name = models.CharField(max_length=64, unique=True)
