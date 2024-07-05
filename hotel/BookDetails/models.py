from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import ValidationError

# Create your models here.

class BedField(models.Model):
    Bed_choices = (
        ('King','King Room'),
        ('Twin', 'Twin Room'),
        ('Grand','Grand Executive Suite')   
    )

    bed = models.CharField(max_length=6, choices=Bed_choices, default='King')
    price = models.CharField(max_length=10)


class BookData(models.Model):
    bedtype = models.ForeignKey(BedField,on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    adults = models.PositiveIntegerField(default=2)
    children = models.PositiveIntegerField(default=0)
    
    def clean(self):
        if self.checkout <= self.checkin:
            raise ValidationError('Checkout date must be after checkin date.')
        return super().clean()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Booking from {self.checkin} to {self.checkout} for {self.adults} adults and {self.children} children"




# class MarkCalendar:
#     year = models.IntegerField()
#     month = models.IntegerField()
#     available_dates = JSONField(default=list,null=True,blank=True)
#     non-available_dates = JSONField(default=list,null=True,blank=True)

# class Permissions():