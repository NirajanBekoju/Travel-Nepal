from django.db import models
from datetime import datetime
from accounts.models import Account

class Agency(models.Model):
    name = models.CharField(max_length=200)
    agent_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, limit_choices_to={'is_agency': True},)
    photo = models.ImageField(upload_to = 'images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    registered_date = models.DateTimeField(datetime.now, blank=True)
    

    def __str__(self):
        return self.name