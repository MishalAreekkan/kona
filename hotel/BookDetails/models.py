from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.db.models import JSONField
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your models here.

Bed_choices = (
    ('King','King Room'),
    ('Twin', 'Twin Room'),
    ('Grand','Grand Executive Suite')   
)

class BookingField(models.Model):
    bed = models.CharField(max_length=6, choices=Bed_choices, default='King')
    price = models.CharField(max_length=10)

# class MarkCalendar:
#     year = models.IntegerField()
#     month = models.IntegerField()
#     present_data = JSONField(default=list,null=True,blank=True)
#     absent_data = JSONField(default=list,null=True,blank=True)

# class Permissions():