from django.test import TestCase

# Create your tests here.
from django.utils import timezone
from .models import Episode

#Here we will create some unit tests to verify if the django app is successfully running. 

# We run this command python manage.py tests to see if we get any errors.
class PodcastsTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title = "My Amazing Podcast Episode",
            description = "I made this on my own!",
            pub_date = timezone.now(),
            link = "https://myawesomeshow.com",
            image = "https://image.myawesomeshow.com",
            podcast_name = "My Python Podcast",
            guid = "de194720-7b4c-49e2-a05f-432436d3fetr",
        )

    def test_episode_content(self):
        self.assertEqual(self.episode.description, "I made this on my own!")
        self.assertEqual(self.episode.link, "https://myawesomeshow.com")
        self.assertEqual(
            self.episode.guid, "de194720-7b4c-49e2-a05f-432436d3fetr"
            )
        
    def test_episode_str_representation(self):
        self.assertEqual(
            str(self.episode), "My Python Podcast: My Amazing Podcast Episode"
        )
