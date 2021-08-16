from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from django.utils import timezone

# Create your models here.
# class freelance(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     country = CountryField()
#     phone_number = PhoneNumberField()
#     def __str__(self):
#         return self.user.username
            


class job(models.Model):
        
    MY_CHOICES = (('item_key1', 'Programming'),
              ('item_key2', 'Graphic Design'),
              ('item_key3', 'General'),
              ('item_key4', 'Hardware'),
              ('item_key5', 'Django'))
    LANGUAGES = [
        ('EN', 'English'),
        ('AR', 'Arabic'),
    ]
    date_posted = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    finished = models.BooleanField(default=False)
    price = models.FloatField()
    language = models.CharField(max_length=30, null=False, choices=LANGUAGES, default='EN')
    categories = MultiSelectField(choices=MY_CHOICES, default="General")
    description = models.TextField()


class reviews(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    reviewee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='other', null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    description = models.TextField()


class transactions(models.Model):
    jobID = models.ForeignKey(job, on_delete=models.CASCADE)
    workerID = models.ForeignKey(User, on_delete=models.CASCADE)
    finished_on = models.DateTimeField(default=timezone.now)

# class category(models.Model):
#     jobID = models.ManyToManyField(job)
#     category = models.CharField(max_length=30)



