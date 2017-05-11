from django.db import models

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
