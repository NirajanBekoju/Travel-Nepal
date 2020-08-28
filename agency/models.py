from django.db import models
from datetime import datetime
from accounts.models import Account
import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/%Y/%m/%d/', filename)

class Agency(models.Model):
    name = models.CharField(max_length=200)
    managing_director = models.CharField(max_length=200)
    agent_id = models.OneToOneField(Account, on_delete=models.DO_NOTHING, limit_choices_to={'is_agency': True}, unique=True)
    photo = models.ImageField(upload_to = get_file_path)
    description = models.TextField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    registered_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to = get_file_path)
    location = models.CharField(max_length=100)
    agency_id = models.ForeignKey(Agency, on_delete=models.DO_NOTHING, limit_choices_to={'is_active': True},)
    is_display = models.BooleanField(default=True)
    booking_date_limit = models.DateTimeField()
    registered_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title