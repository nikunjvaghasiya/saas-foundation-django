from django.db import models

class PageVisit(models.Model):
    page = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)