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
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]+'...'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')




