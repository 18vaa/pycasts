from django.apps import AppConfig


class PodcastsConfig(AppConfig):

    #This line ensures that our Django app is configured to  add a primary key to all the models automatically.
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'podcasts'
