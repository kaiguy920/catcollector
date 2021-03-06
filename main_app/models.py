from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# this double underscore(dunder) method controls what happens when we print one of these objects


def __str__(self):
    return self.name

# here is our cat toy model


class CatToy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cattoys_detail', kwargs={'cattoy_id': self.id})


class Cat(models.Model):
    # user comes from Django, has pre-build properties(& methods)
    # we set up our foreign key reference
    # tell it which model we're referring to (User)
    # and the second agument (on_delete) says to delete all resources that are owned by the user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # this is where we setup our columns & data types
    # this is similar to our mongoose schemas/models
    # we set the key with it's name, then tell what type of data to expect
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()
    # here we are using django's built in manytomany field
    # this does a LOT for us, including dealing with join tables
    cattoys = models.ManyToManyField(CatToy)
