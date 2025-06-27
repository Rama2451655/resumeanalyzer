from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    file = models.FileField(upload_to='resumes/')
    skills = models.TextField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)   