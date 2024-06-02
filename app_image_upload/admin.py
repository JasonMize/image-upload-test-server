from django.contrib import admin
from app_image_upload.models import *


class ImageAdmin(admin.ModelAdmin):
  pass

class ProfileAdmin(admin.ModelAdmin):
  pass


admin.site.register(Image, ImageAdmin)
admin.site.register(Profile, ProfileAdmin)
