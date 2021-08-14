from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """Post model."""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='liked')
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        """Return title and username"""
        return f'{self.title} By @{self.user.username}'
    
    @property
    def num_likes(self):
        return self.likes.all().count()