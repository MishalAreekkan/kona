from django.urls import path
from . import views

urlpatterns = [
    path('bookField',views.bookField,name='bookField'),
    path('payment/<int:id>/', views.payment, name='payment'),
    path('booking/<int:id>/<int:year>/<int:month>/',views.booking,name='booking'),
    path('paysuccess/<int:id>/', views.payment_success, name='paysuccess'),
    path('payfailed/<int:id>/', views.payment_failed, name='payfailed'),
]
