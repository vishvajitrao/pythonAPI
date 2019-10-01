from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from .models import Person, Registration
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from myapp.serializers import MyappSerializer

from .forms import *
from django.contrib.auth.models import User


# Create your views here.

def firstProject(request):
    return HttpResponse("<h1>This is first project</h1>")


class PersonList(ListView):
    model = Person
    context_object_name = 'index'


class PersonDetails(DetailView):
    model = Person


class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'email', 'number']
    success_url = '/users'


class PersonDelete(DeleteView):
    model = Person
    success_url = '/users'


class CreateUser(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'email', 'number']
    success_url = '/users'


# Django rest framework

class MyappList(APIView):
    def get(self, request):
        myapp = Person.objects.all()
        serializer = MyappSerializer(myapp, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MyappSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyappDetail(APIView):
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        myapp = self.get_object(pk)
        serializer = MyappSerializer(myapp)
        return Response(serializer.data)

    def put(self, request, pk):
        myapp = self.get_object(pk)
        serializer = MyappSerializer(myapp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        myapp = self.get_object(pk)
        myapp.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


# Django User Registration Form

def register(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            #return redirect('/register')
        messages.success(request,'Registration Successfully....')
    else:
        form = userForm()
    return render(request, 'registration_form.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = auth.authenticate(username = username, password = password)
            if user is not None:
                auth.login(request, user)
                return render(request,'welcome.html')
            else:
                messages.error(request, 'Invalid Credential')
        except Exception as ex:
            print("User name and password is not correct",ex)
    return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')


def status(request):
    return render(request, 'status.html')


def customRegistration(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email') and request.POST.get('pnumber') and request.POST.get('password'):
            form = Registration()
            form.username = request.POST.get('username')
            form.first_name = request.POST.get('first_name')
            form.last_name = request.POST.get('last_name')
            form.email = request.POST.get('email')
            form.phone_number = request.POST.get('pnumber')
            form.password = request.POST.get('password')
            form.save()
            messages.success(request, 'Registration Successfully....')
            return render(request, 'custom_registration.html')
    else:
        return render(request, 'custom_registration.html')


