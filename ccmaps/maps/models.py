from django.db import models
from django.contrib.auth.models import User

class Map(models.Model):
    name = models.CharField(max_length=50)
    uploader = models.ForeignKey(User)
    first_uploaded = models.DateField()
    author = models.CharField(max_length=50)
    description = models.TextField()
        
    
class MapRevision(models.Model):
    map = models.ForeignKey(Map)
    version_serial = models.IntegerField()
    uploaded = models.DateField()
    change_desc = models.TextField()
    file = models.FileField(upload_to='user_maps')
    properties = models.ForeignKey('MapProperties')
    
class MapProperties(models.Model):
    GAMES = (
        (u'RA2', u'Red Alert 2'),
        (u'YR', u'Yuri''s Revenge'),
        (u'TS', u'Tiberian Sun'),
        (u'FS', u'Firestorm'),
        (u'RA2', u'Red Alert 1'),
        (u'TD', u'Tiberian Dawn'),
    )
    
    THEATERS = (
        (u'TEM', u'Temperate'),
        (u'SNO', u'Snow'),
        (u'URB', u'Urban'),
        (u'UBN', u'New Urban'),
        (u'LUN', u'Lunar'),
        (u'DES', u'Desert'),
    )

    min_players = models.IntegerField()
    max_player = models.IntegerField()
    theater = models.CharField(max_length=3, choices=THEATERS)
    game = models.CharField(max_length=50, choices=GAMES)
    ore_estimate = models.IntegerField()
    gems_estimate = models.IntegerField()
    num_oil_derricks = models.IntegerField()
    height_variation_idx = models.FloatField()