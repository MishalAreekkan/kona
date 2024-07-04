import datetime
from . models import BookingField
from home.models import StayPics
def check_available(name,checkin,checkout):
    empty = []
    booked_list = StayPics.objects.filter(name=name )
    # for booked in booked_list: