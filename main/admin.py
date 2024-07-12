from django.contrib import admin
from . import models

admin.site.register(models.Blog)
admin.site.register(models.Comment)
admin.site.register(models.User)
admin.site.register(models.SocialMedia)