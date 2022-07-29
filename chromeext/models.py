from django.db import models
# Create your models here.

class Destination(models.Model):
    id = int
    img = models.ImageField(upload_to='pics')

class Meta:
        db_table = "chromeext_destination"
      