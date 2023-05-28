from django.contrib import admin

# Register your models here.

#This is to make sure that the admin (me) can interact with the episodes stored in the database.

#Admin can also specify which data to display, like I have done using list_display.
from .models import Episode

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("podcast_name","title","pub_date")