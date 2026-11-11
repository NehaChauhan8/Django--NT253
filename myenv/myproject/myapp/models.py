from django.db import models

# Create your models here.
class Emp(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()

    #to display the name of the employee in the admin panel instead of object we need to define the __str__ method
    def __str__(self):
        return self.firstname

class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    description=models.CharField(max_length=200)

    #to display the name of the author in the admin panel instead of object we need to define the __str__ method
    def __str__(self):
        return self.name


class Books(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    published_date=models.DateField()

    #to display the title of the book in the admin panel instead of object we need to define the __str__ method
    def __str__(self):
        return self.title

class Blogpost(models.Model):
    title = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title