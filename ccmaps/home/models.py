from django.db import models
from django.contrib.auth.models import User

class CNCMap(models.Model):
    name = models.CharField(max_length=50)
    uploader = models.ForeignKey(User)
    first_uploaded = models.DateField()
    author = models.CharField(max_length=50)
    description = models.TextField()
        
    
class CNCMapRevision(models.Model):
    map = models.ForeignKey(CNCMap)
    version_serial = models.IntegerField()
    uploaded = models.DateField()
    change_desc = models.TextField()
    file = models.FileField(upload_to="user_maps")
    metadata = models.ForeignKey("CNCMapMetadata")
    
class CNCMapMetadata(models.Model):
    GAMES = (
        (u'RA2', u'Red Alert 2'),
        (u'YR', u'Yuri''s Revenge'),
        (u'TS', u'Tiberian Sun'),
        (u'FS', u'Firestorm'),
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