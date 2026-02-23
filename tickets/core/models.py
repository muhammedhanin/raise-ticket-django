from django.db import models

class Ticket(models.Model):
    title = models.CharField(max_length = 1000)
    description = models.CharField(max_length = 1000)
    category = models.CharField(max_length = 100)
    priority = models.CharField(max_length = 100)