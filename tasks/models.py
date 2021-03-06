from django.db import models

# Create your models here.

class Task(models.Model):
        title = models.name = models.CharField(max_length=200)
        # line = models.name = models.CharField(max_length=200)
        # complete = models.BooleanField(default=False)
        # created = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return self.title


class TaskLine(models.Model):
        task = models.ForeignKey(Task, on_delete=models.CASCADE)
        line = models.name = models.CharField(max_length=200)

        def __str__(self):
                return self.line