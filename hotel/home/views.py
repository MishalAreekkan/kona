from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from datetime import datetime
import sweetify
from .forms import RegisterationForm, LoginForm, StayPicsForm, DinePicsForm
from .models import StayPics, DinePics,MyUser


def register(req):
    if req.method == 'POST':
        form = RegisterationForm(req.POST)
        if form.is_valid():
            MyUser.objects.create_user(**form.cleaned_data)
            return redirect('login')
    else:
        form = RegisterationForm()
    return render(req, 'regi/register.html', {'form': form})


def user_login(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            user = MyUser.objects.get(username = form.cleaned_data['username'])
            if user.check_password(form.cleaned_data['password']):
                login(req, user)
                sweetify.toast(req, 'You have successfully logged in.')
                return redirect('stay')
            else:
                sweetify.toast(req, 'Oops, something went wrong!', icon="error", timer=2000)
    else:
        form = LoginForm()
    return render(req, 'regi/login.html', {"form": form})


def user_logout(req):
    logout(req)
    sweetify.toast(req, 'You have successfully logged out.')
    return redirect('login')


def roompic(request):
    if request.method == 'POST':
        form = StayPicsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stay')
    else:
        form = StayPicsForm()
    # show = StayPics.objects.all()
    context = {
        'form': form,
        # 'show': show
    }
    return render(request, 'navbar/Stay_pics.html',context )


def stay_pic_edit(req, id):
    # edited = get_object_or_404(StayPics, id=id)
    edited = StayPics.objects.get(id=id)
    if req.method == 'POST':
        form = StayPicsForm(req.POST, instance=edited)
        if form.is_valid():
            form.save()
            return redirect('roompic')
    else:
        form = StayPicsForm(instance=edited)
    return render(req, 'navbar/Stay_pics_edit.html', {'form': form, 'id': id})


def stay_delete(req, id):
    deleting = get_object_or_404(StayPics, id=id)
    deleting.delete()
    return redirect('roompic')


def dinepic(req):
    if req.method == 'POST':
        form = DinePicsForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('dine')
    else:
        form = DinePicsForm()
    return render(req, 'navbar/DinePics.html', {'form': form})


def home(req):
    sweetify.success(req, 'Cheers to new toast')
    sweetify.toast(req, 'Cheers to new toast')
    return render(req, 'navbar/home.html')


def stay(req):
    images = StayPics.objects.all()
    return render(req, 'navbar/stay.html', {'images': images})


def dine(req):
    dine_images = DinePics.objects.all()
    return render(req, 'navbar/dine.html', {'dine': dine_images})


def spa(req):
    return render(req, 'navbar/spa.html')


def celebrate(req):
    return render(req, 'navbar/celebrate.html')


def gallery(req):
    return render(req, 'navbar/gallery.html')




def url_date(req, id=None):
        today = datetime.today()
        year = today.year
        month = today.month
        return redirect('booking', id=id, year=year, month=month)

