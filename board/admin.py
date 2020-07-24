from django.contrib import admin
from . import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    # can custom admin page here
    pass


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    pass

