from django.db import models

# Create your models here.
class Region(models.Model):
	NORTH_AMERICA = 'NA'
	EUROPE = 'EU'
	REGION_CHOICES = (
		(NORTH_AMERICA, 'North America'),
		(EUROPE, 'Europe'),
	)
	soccer_region = models.CharField(max_length=2, choices=REGION_CHOICES, default=NORTH_AMERICA)

class NATeam(models.Model):
	NORTH_AMERICA = 'NA'
	EUROPE = 'EU'
	REGION_CHOICES = (
		(NORTH_AMERICA, 'North America'),
		(EUROPE, 'Europe'),
	)
	soccer_region = models.CharField(max_length=2, choices=REGION_CHOICES, default=NORTH_AMERICA)

class EUTeam(models.Model):
	NORTH_AMERICA = 'NA'
	EUROPE = 'EU'
	REGION_CHOICES = (
		(NORTH_AMERICA, 'North America'),
		(EUROPE, 'Europe'),
	)
	soccer_region = models.CharField(max_length=2, choices=REGION_CHOICES, default=NORTH_AMERICA)