from django.contrib import admin
from .models import Person, Registration, Blog, Entry, Author,EntryDetail, Authors, Book, Publisher, Store, Laptop, Student


# Register your models here.
admin.site.register(Person)
admin.site.register(Registration)
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Author)
admin.site.register(EntryDetail)

admin.site.register(Authors)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Store)
admin.site.register(Laptop)
admin.site.register(Student)
