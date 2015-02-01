from django.db import models

# Create your models here.
class Region(models.Model):
	name = models.CharField(max_length=30)

	'''
	NORTH_AMERICA = 'NA'
	EUROPE = 'EU'
	REGION_CHOICES = (
		(NORTH_AMERICA, 'North America'),
		(EUROPE, 'Europe'),
	)
	region = models.CharField(max_length=3, choices=REGION_CHOICES, default=USA)
	'''

	def __str__(self):
		return self.name

class NATeam(models.Model):
	name = models.CharField(max_length=30)

	'''
	SEATTLE_SOUNDERS = 'SEA'
	NEW_YORK_REDBULLS = 'NYR'
	LA_GALAXY = 'LAG'
	TORONTO_FC = 'TFC'
	NEW_ENGLAND_REVOLUTION = 'REV'
	CHIVAS_USA = 'CHS'
	NEW_YORK_CITY_FC = 'NYC'
	PORTLAND_TIMBERS = 'POR'
	VANCOUVER_WHITECAPS_FC = 'VAN'
	PHILADELPHIA_UNION = 'PHI'
	REAL_SALT_LAKE = 'RSL'
	DC_UNITED = 'DCU'
	COLUMBUS_CREW_SC = 'COL'
	SAN_JOSE_EARTHQUAKES = 'SJE'
	ORLANDO_CITY_SC = 'ORL'
	HOUSTON_DYNAMO = 'HOU'
	FC_DALLAS = 'DAL'
	MONTREAL_IMPACT = 'MTL'
	CHICAGO_FIRE_SOCCER_CLUB = 'CHI'
	COLORADO_RAPIDS = 'CDO'
	ATLANTA_MLS_TEAM = 'ATL'
	
	NATEAM_CHOICES = (
		(SEATTLE_SOUNDERS, 'Seattle Sounders'),
		(NEW_YORK_REDBULLS, 'New York Redbulls'),
		(LA_GALAXY, 'LA Galaxy'),
		(TORONTO_FC, 'Toronto FC'),
		(NEW_ENGLAND_REVOLUTION, 'New England Revolution'),
		(CHIVAS_USA, 'Chivas USA'),
		(NEW_YORK_CITY_FC, 'NYC FC'),
		(PORTLAND_TIMBERS, 'Portland Timbers'),
		(VANCOUVER_WHITECAPS_FC, 'Vancouver Whitecaps'),
		(PHILADELPHIA_UNION, 'Philadelphia Union'),
		(REAL_SALT_LAKE, 'Real Salt Lake'),
		(DC_UNITED, 'DC United'),
		(COLUMBUS_CREW_SC, 'Columbus Crew'), 
		(SAN_JOSE_EARTHQUAKES, 'San Jose Earthquaks'),
		(ORLANDO_CITY_SC, 'Orlando City FC'),
		(HOUSTON_DYNAMO, 'Houston Dynamo'),
		(FC_DALLAS, 'FC Dallas'),
		(MONTREAL_IMPACT, 'Montreal Impact'),
		(CHICAGO_FIRE_SOCCER_CLUB, 'Chicago Fire'),
		(COLORADO_RAPIDS, 'Colorado Rapids'),
		(ATLANTA_MLS_TEAM, 'Atanta'),
	)
	team = models.CharField(max_length=4, choices=NATEAM_CHOICES, default=SEATTLE_SOUNDERS)
	region = models.ForeignKey(Region)
	'''

	def __str__(self):
		return self.name


class EUTeam(models.Model):
	name = models.CharField(max_length=30)

	'''
	REAL_MADRID = 'MAD'
	BARCELONA = 'BAR'
	ATLETICO_MADRID = 'ATL'
	MANCHESTER_CITY = 'MCY'
	CHELSEA = 'CHE'
	ARSENAL = 'ARS'
	LIVERPOOL = 'LIV'
	MANCHESTER_UNITED = 'MNU'
	TOTTENHAM = 'TOT'
	PSG = 'PSG'
	OLYMPIQUE_LYONNAISE = 'OL'
	AC_MILAN = 'MIL'
	JUVENTUS = 'JUV'
	INTER_MILAN = 'INT'
	NAPOLI = 'NAP'
	ROMA = 'ROMA'
	BAYERN_MUNICH = 'BMU'
	BORRUSIA_DORTMUND = 'BOR'

	EUTEAM_CHOICES = (
		(REAL_MADRID, 'Real Madrid'),
		(BARCELONA, 'Barcelona'),
		(ATLETICO_MADRID, 'Atletico Madrid'),
		(MANCHESTER_CITY, 'Manchester City'),
		(CHELSEA, 'Cheslea'),
		(ARSENAL, 'Arsenal'),
		(LIVERPOOL, 'Liverpool'),
		(MANCHESTER_UNITED, 'Manchester United'),
		(TOTTENHAM, 'Tottenham Hotspur'),
		(PSG, 'Paris St. Germain'),
		(OLYMPIQUE_LYONNAISE, 'Lyon'),
		(AC_MILAN, 'AC Milan'),
		(JUVENTUS, 'Juventus'),
		(INTER_MILAN, 'Inter Milan'),
		(NAPOLI, 'Napoli'),
		(ROMA, 'Roma'),
		(BAYERN_MUNICH, 'Bayern Munich'),
		(BORRUSIA_DORTMUND, 'Borussia Dortmund'),
	)
	team = models.CharField(max_length=4, choices=EUTEAM_CHOICES, default=REAL_MADRID)
	region = models.ForeignKey(Region)
	'''

	def __str__(self):
		return self.name


