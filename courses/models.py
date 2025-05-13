from django.db import models
from users.models import Professor

class Course(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='courses')
    discipline = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
