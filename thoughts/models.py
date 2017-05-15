from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    avatar = models.FileField(null=True, blank=True)
    user = models.OneToOneField('auth.User')
    random_url = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.get_full_name()

class Category(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey('auth.User')
    random_url = models.CharField(max_length=20, blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

    @property
    def get_posts(self):
        return Blog.objects.filter(category=self)

class Blog(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    random_url = models.CharField(max_length=20, blank=True, null=True, unique=True)

    def __str__(self):
        return self.title
