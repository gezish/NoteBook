from django.db import models



class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    dob = models.DateField()
    bio = models.TextField()
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.name
