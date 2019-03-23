from django.db import models

# Create your models here.
# Title
# Publication Date
# Body
# Image


# Add the Blog app to the settings
# Create a migrations
# Migrate
# Add to the Admin

class Blog(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField('date published')
    body = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')



