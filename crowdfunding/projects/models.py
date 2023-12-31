from django.db import models
from django.contrib.auth import get_user_model

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.FloatField()
    image = models.URLField(max_length=200,default='https://picsum.photos/600')
    is_open = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    is_deleted = models.BooleanField(default=False)

class Pledge(models.Model):
    amount = models.FloatField()
    comment = models.CharField(max_length=200, null=True)
    anonymous = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    is_deleted = models.BooleanField(default=False)