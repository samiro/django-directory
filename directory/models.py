from __future__ import unicode_literals

from django.db import models


class City(models.Model):
    slug = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=50)
    demonym = models.CharField(max_length=30, blank=True, null=True)
    form = models.URLField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.title


class Neighborhood(models.Model):
    city = models.ForeignKey(City)
    title = models.CharField(max_length=20)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return '%s - %s' % (self.title, self.city.title)


class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=150)

    def __unicode__(self):
        return self.title

    def get_count(self, city):
        return self.business_set.filter(city=city).count()


class Business(models.Model):
    neighborhood = models.ForeignKey(Neighborhood)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=100, blank=True)
    schedule = models.TextField(max_length=500, blank=True)
    phones = models.CharField(max_length=500, blank=True, help_text='PHONE;PHONE')
    whatsapp = models.CharField(max_length=50, blank=True, help_text='Solo uno')
    link = models.URLField(max_length=100, blank=True, null=True)
    delivery = models.CharField(max_length=500, blank=True, help_text='APP@LINK;APP@LINK')
    has_delivery = models.BooleanField(default=False)
    has_takeout = models.BooleanField(default=False)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    def get_phones(self):
        return self.phones.split(';')

    def get_delivery(self):
        return [d.split('@') for d in self.delivery.split(';')]
