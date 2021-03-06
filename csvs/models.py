from django.db import models
from django.urls import reverse


class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded_time = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    

    def __str__(self):
        return f'File id: {self.id}, File Name: {self.file_name}'
    

    def get_absolute_url(self):
        return reverse('home')
