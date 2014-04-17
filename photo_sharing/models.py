from django.db import models
from django.contrib.auth.models import User
#from registration.models import User 

import os
from string import join
from PIL import Image as PImage

MEDIA_ROOT = '/home/kyaw/Documents/env/mlickr/media/' # its host dependable



class HashTag(models.Model):
	hashtag = models.CharField(max_length=50, blank=True)
	def __unicode__(self):
		return self.hashtag

class Album(models.Model):
	title = models.CharField(max_length=100)

	def __unicode__(self):
		return self.title
		


class Image(models.Model):
	title = models.CharField(max_length=60, blank=True, null=True)
	image = models.FileField(upload_to="images/")
	hashtags = models.ManyToManyField(HashTag, blank=True)
	albums = models.ManyToManyField(Album, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=50)
	width = models.IntegerField(blank=True, null=True)
	height = models.IntegerField(blank=True, null=True)
	user = models.ForeignKey(User, null=True, blank=True)

	def save(self, *args, **kwargs):
		super(Image, self).save(*args, **kwargs)
		img = PImage.open(os.path.join(MEDIA_ROOT, self.image.name))
		self.width, self.height = img.size 
		super(Image, self).save(*args, **kwargs)

	def size(self):
		return "%s X %s" % (self.width, self.height)	

	def __unicode__(self):
		return self.image.name 

	def hashtags_(self):
		lst = [x[1] for x in self.hashtags.values_list()]
		return str(join(lst, ','))

	def albums_(self):
		lst = [x[1] for x in self.albums.values_list()]
		return str(join(lst, ','))

	def thumbnail(self):
		return """<a href="/media/images%s"><img border="0" alt="" src="/media/images%s" height="40" /></a>""" % (
                                                                    (self.image.name, self.image.name))

	thumbnail.allow_tags = True



