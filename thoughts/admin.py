from django.contrib import admin
from thoughts.models import Blog, Category, Profile, Reply

admin.site.register([Blog, Category, Profile, Reply])
