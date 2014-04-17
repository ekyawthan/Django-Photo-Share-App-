from django.contrib import admin
from models import Image , HashTag, Album



class AlbumAdmin(admin.ModelAdmin):
	search_field = ["title"]
	list_display = ["title"]

class HashTagAdmin(admin.ModelAdmin):
	list_display = ["hashtag"]


class ImageAdmin(admin.ModelAdmin):
	search_field = ["title"]
	list_display = ["__unicode__", "title", "rating","size", "created", "hashtags_", "thumbnail"]
	list_filter = ["hashtags", "albums"]

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()



admin.site.register(Album, AlbumAdmin)
admin.site.register(HashTag, HashTagAdmin)
admin.site.register(Image, ImageAdmin)

