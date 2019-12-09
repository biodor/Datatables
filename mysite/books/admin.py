from django.contrib import admin

from .models import Comment, Book

admin.site.register(Comment)
admin.site.register(Book)