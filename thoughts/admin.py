from django.contrib import admin
from thoughts.models import Blog, Category

admin.site.register([Blog, Category])
