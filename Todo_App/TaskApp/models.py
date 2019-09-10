from django.db import models

# Create your models here.
class TaskDetails(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    progress = (('p','In Progress'),
                ('c','Completed'),
                ('pen','Pending'))
    status = models.CharField(max_length=50)
