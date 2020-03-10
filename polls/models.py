from django.contrib.auth.models import User
from django.db import models
import datetime
# Create your models here.
class Poll(models.Model):
    subject = models.CharField(max_length=30)
    detail = models.TextField()
    picture = models.FileField(upload_to='documents/%Y/%m/%d')
    password = models.CharField(max_length=100, null=True)
    start_date = models.DateTimeField(default=datetime.datetime.now())
    end_date = models.DateTimeField(null=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=datetime.datetime.now())
    duration = models.IntegerField(default=0)
    def __str__(self):
        return self.subject
class Poll_Choice(models.Model):
    subject = models.CharField(max_length=30) 
    image = models.ImageField(upload_to='choice/%Y/%m/%d')
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
class Poll_Vote(models.Model):
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Poll_Choice, on_delete=models.CASCADE)
    vote_by = models.ForeignKey(User, on_delete=models.CASCADE)