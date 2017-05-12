from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    avatar = models.FileField(null=True, blank=True)
    user = models.OneToOneField('auth.User')

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.get_full_name()

class Category(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey('auth.User')

    def __str__(self):
        return self.title

class Blog(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    public = models.BooleanField(default=False)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title
