from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length = 24)
    email = models.EmailField()
    tel_number = models.IntegerField()
    avatar = models.ImageField(upload_to='posts/static/posts')
    registered_time = models.DateTimeField()

    def __str__(self):
        return self.username
