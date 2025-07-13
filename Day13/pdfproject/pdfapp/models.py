# pdfapp/models.py

from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.title
