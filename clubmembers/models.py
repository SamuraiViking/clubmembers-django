from django.db import models 

class Post(models.Model):
    title=models.CharField(max_length=120, help_text='title of message.')
    message = models.TextField(help_text="Whats on your mind ... ")

    def __str__(self):
        return self.title

class ClubMember(models.Model):
    email=models.EmailField(max_length=254)
    display_name=models.CharField(max_length=120, default="")
    photo=models.URLField(max_length=200, default="")

    def __str__(self):
        return self.email
