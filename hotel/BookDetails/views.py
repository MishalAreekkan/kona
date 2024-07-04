from django.shortcuts import render,redirect
import sweetify
from django.views.generic import ListView
from .models import BookingField
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
import uuid
from home.models import StayPics
from BookDetails.forms import BookingForm
from BookDetails.models import BookingField


# Create your views here.

def bookField(req):
    pass


@login_required(login_url='login')
def booking(req, id, year=None, month=None, *args, **kwargs,):
    book = get_object_or_404(StayPics, id=id)
    form = BookingForm()
    if req.method == 'POST':
        form = BookingForm(req.POST)
        if form.is_valid(): 
            checkin = form.cleaned_data['checkin']
            checkout = form.cleaned_data['checkout']
            bed = form.cleaned_data['bed']
            adults = form.cleaned_data['adults']
            children = form.cleaned_data['children']

            existing_reservation = BookingField.objects.filter(
                bed=bed,
                checkin__lt=checkout,
                checkout__gt=checkin
            ).exists()

            if existing_reservation:
                sweetify.toast(req, 'Room has already been reserved', icon='warning', timer=3000)
                return render(req, "booking/booking.html", {'form': form, 'book': book, 'year': year, 'month': month,"paypal":paypal})

            data = BookingField.objects.create(
                customer=req.user,
                bed=bed,
                checkin=checkin,
                checkout=checkout,
                adults=adults,
                children=children,
            )
        else:
            print(form.error)
    host = req.get_host()               
    paypal_payment = {
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                'item_name': book.room,
                'invoice': uuid.uuid4(),
                'currency_code': 'USD',
                'notify_url': f"http://{host}{reverse('paypal-ipn')}",
                'return_url': f"http://{host}{reverse('paysuccess', kwargs={'id': id})}",
                'cancel_url': f"http://{host}{reverse('payfailed', kwargs={'id': id})}",  
            }
    paypal = PayPalPaymentsForm(initial=paypal_payment)

    context = {
        'id': id,
        'book': book,
        'form': form,
        'year': year,
        'month': month,
        "paypal":paypal
    }
    sweetify.toast(req, 'Booking completed successfully.')
    return render(req, 'booking/booking.html', context)



def payment(req,id):  
    return render(req,'payment/payment.html')

def payment_success(request, id):
    return render(request, 'payment/payment_success.html', {'id': id})

def payment_failed(request, id):
    return render(request, 'payment/payment_failed.html', {'id': id})
    
    
class BookedList(ListView):
    model = BookingField