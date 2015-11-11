# -*- coding: utf-8 -*-
from django.contrib.gis.db import models

class State(models.Model):
    name = models.CharField(max_length=50)
    #density = models.IntegerField()
    statefp = models.IntegerField()

    #population = models.IntegerField(null=False, default=0)
    #areaInKm = models.IntegerField(null=True)
    #attribute name "geom" mandatory for django-geojson
    geom = models.MultiPolygonField(srid=4326)
    #africanAmericanPopulation = models.IntegerField(null=True)
    #About GeoManager see :
    #https://docs.djangoproject.com/en/1.8/ref/contrib/gis/model-api/
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    state_mapping = {
        'statefp' : 'STATEFP',
        'name' : 'NAME',
        'geom' : 'POLYGON25D',
    }

    # getDensityInSQ
    # getAreaInSQ
    # getAApourcentage
    # 

class County(models.Model):
    statefp = models.IntegerField(null=False)
    countyfp = models.IntegerField(null=False)
    name = models.CharField(max_length=100)
    geom = models.MultiPolygonField(srid=4326)
    state = models.ForeignKey(State, default=1)

    objects = models.GeoManager()

    # Auto-generated `LayerMapping` dictionary for County model
    county_mapping = {
        'statefp' : 'STATEFP',
        'countyfp' : 'COUNTYFP',
        'name' : 'NAME',
        'geom' : 'POLYGON25D',
    }
    def __unicode__(self):
        return self.name
