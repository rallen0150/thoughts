from django.contrib import admin
from thoughts.models import Blog, Category, Profile

admin.site.register([Blog, Category, Profile])
