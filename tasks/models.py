from django.db import models

# Create your models here.

class Task(models.Model):
        title = models.name = models.CharField(max_length=200)
        descr = models.name = models.TextField(max_length=750, default='Before Description')
        complete = models.BooleanField(default=False)
        created = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return self.title