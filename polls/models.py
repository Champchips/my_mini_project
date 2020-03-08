from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Poll(models.Model):
    subject = models.CharField(max_length=30)
    detail = models.TextField()
    picture = models.ImageField()
    passsword = models.CharField(max_length=100, null=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.subject
class Poll_Choice(models.Model):
    subject = models.CharField(max_length=30) 
    image = models.ImageField()
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
class Poll_Vote(models.Model):
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Poll_Choice, on_delete=models.CASCADE)
    vote_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    