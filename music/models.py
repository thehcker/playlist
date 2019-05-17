import random
import os
from django.db import models
from django.urls import reverse


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "music/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )

# Create your models here.
class Album(models.Model):
	artist = models.CharField(max_length=100)
	album_title = models.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	album_logo = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	is_favorite = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('music:detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.album_title + '-' + self.artist


class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	audio_file = models.FileField(default='')
	song_title = models.CharField(max_length=100)
	is_favorite = models.BooleanField(default=False)

	def __str__(self):
		return self.song_title
