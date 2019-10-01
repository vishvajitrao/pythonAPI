from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length = 20,help_text = "Please enter First Name")
    last_name = models.CharField(max_length = 20,help_text = "Please enter Last Name")
    email = models.EmailField(max_length = 50,help_text = "Please enter email")
    number = models.IntegerField()

class Registration(models.Model):
    username = models.CharField(max_length=20,help_text="Please enter first name here ")
    first_name = models.CharField(max_length=20,help_text="Please enter first name here ")
    last_name = models.CharField(max_length=20,help_text="Please enter first name here ")
    email = models.EmailField(max_length=50,help_text="Please enter first name here ")
    phone_number = models.IntegerField(help_text="Please enter first name here ")
    password = models.CharField(max_length=20,help_text="Please enter first name here ")

    def __str__(self):
        return self.first_name

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.headline

class EntryDetail(models.Model):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE)
    details = models.TextField()


# Aggregation

class Authors(models.Model):
    name = models.CharField(max_length= 30)
    age = models.IntegerField()

class Publisher(models.Model):
    name = models.CharField(max_length= 30)


class Book(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    authors = models.ManyToManyField(Authors)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)


# Django Model Manager

class Laptop(models.Model):
    name = models.CharField(max_length= 30)
    ram = models.CharField(max_length=10)
    laptop = models.Manager()


# Performing raw sql query in Django

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    birth_date = models.DateField()

    def __str__(self):
        return str(self.first_name) +' ' + str(self.last_name)

