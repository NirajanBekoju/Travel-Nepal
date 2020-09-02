from django.db import models
from agency.models import Event
from accounts.models import Account

# Create your models here.
class Inquiry(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    event_id = models.ForeignKey(Event, on_delete=models.DO_NOTHING, limit_choices_to={'is_display': True},)
    user_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, limit_choices_to={'is_agency': False})
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
