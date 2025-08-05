from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    reputation = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Confession(models.Model):
    CATEGORY_CHOICES = [
        ('funny', 'Funny'),
        ('crush', 'Crush'),
        ('life', 'Life'),
        ('work', 'Work'),
    ]
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    anonymous_name = models.CharField(max_length=50, default='Anonymous')
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    latitude = models.FloatField()
    longitude = models.FloatField()
    reactions_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()


class Reaction(models.Model):
    confession = models.ForeignKey(Confession, on_delete=models.CASCADE, related_name="reactions")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
