from django.contrib import admin
from .models import Books, Emp, Author

# Register your models here.
admin.site.register(Emp)
admin.site.register(Author)
admin.site.register(Books)
