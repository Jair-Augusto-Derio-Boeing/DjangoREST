from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        abstract = True  # Não cria tabela para Person


class Student(Person):
    ra = models.CharField(max_length=50)


class Professor(Person):
    siape = models.CharField(max_length=50)
