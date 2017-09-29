from django.db import models


class City(models.Model):
    city = models.CharField(max_length=140)

    def __str__(self):
        return u'%s' % (self.city)


class Country(models.Model):
    country = models.CharField(max_length=140)

    def __str__(self):
        return u'%s' % (self.country)

class Course(models.Model):
    name = models.CharField(max_length=140)
    country = models.ForeignKey(Country, default=1, blank=True, null=True)
    city = models.ForeignKey(City, default=1, blank=True, null=True)
