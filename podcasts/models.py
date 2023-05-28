from django.db import models

# Create your models here.

#My Episode class needs to have title, description, publication date, link, image, name of the podcast and a guid
class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    podcast_name = models.CharField(max_length=100)
    guid = models.CharField(max_length=50)



    def __str__(self) -> str:
        return f"{self.podcast_name}: {self.title}"