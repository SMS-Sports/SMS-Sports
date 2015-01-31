from django.db import models

# Create your models here.
class Region(models.Model):
	USA = 'USA'
	EUROPE = 'EU'
	REGION_CHOICES = (
		(USA, 'USA'),
		(EUROPE, 'Europe'),
	)
	soccer_region = models.CharField(max_length=2, choices=REGION_CHOICES, default=NORTH_AMERICA)

class NATeam(models.Model):
	SEATTLE SOUNDERS = 'SEA'
	NEW YOUR REDBULLS = 'NYR'
	LA GALAXY = 'LAG'
	TORONTO FC = 'TFC'
	NEW ENGLAND REVOLUTION = 'REV'
	CHIVAS USA = 'CHS'
	NEW YORK CITY FC = 'NYC'
	PORTLAND TIMBERS = 'POR'
	VANCOUVER WHITECAPS FC = 'VAN'
	PHILADELPHIA UNION = 'PHI'
	REAL SALT LAKE = 'RSL'
	D.C. UNITED = 'DCU'
	COLUMBUS CREW SC = 'COL'
	SAN JOSE EARTHQUAKES = 'SJE'
	ORLANDO CITY SC = 'ORL'
	HOUSTON DYNAMO = 'HOU'
	FC DALLAS = 'DAL'
	MONTREAL IMPACT = 'MTL'
	CHICAGO FIRE SOCCER CLUB = 'CHI'
	COLORADO RAPIDS = 'CDO'
	ATLANTA MLS TEAM = 'ATL'
	
	NATEAM_CHOICES = (
		(SEATTLE SOUNDERS, 'Seattle Sounders'),
		(NEW YOUR REDBULLS, 'New York Redbulls'),
		(LA GALAXY, 'LA Galaxy'),
		(TORONTO FC, 'Toronto FC'),
		(NEW ENGLAND REVOLUTION, 'New England Revolution'),
		(CHIVAS USA, 'Chivas USA'),
		(NEW YORK CITY FC, 'NYC FC'),
		(PORTLAND TIMBERS, 'Portland Timbers'),
		(VANCOUVER WHITECAPS FC, 'Vancouver Whitecaps'),
		(PHILADELPHIA UNION, 'Philadelphia Union'),
		(REAL SALT LAKE, 'Real Salt Lake'),
		(D.C. UNITED, 'DC United'),
		(COLUMBUS CREW SC, 'Columbus Crew'), 
		(SAN JOSE EARTHQUAKES, 'San Jose Earthquaks'),
		(ORLANDO CITY SC, 'Orlando City FC'),
		(HOUSTON DYNAMO, 'Houston Dynamo'),
		(FC DALLAS, 'FC Dallas'),
		(MONTREAL IMPACT, 'Montreal Impact'),
		(CHICAGO FIRE SOCCER CLUB, 'Chicago Fire'),
		(COLORADO RAPIDS, 'Colorado Rapids'),
		(ATLANTA MLS TEAM, 'Atanta'),
	)
	soccer_region = models.CharField(max_length=2, choices=REGION_CHOICES, default=NORTH_AMERICA)

class EUTeam(models.Model):
	REAL MADRID = 'MAD'
	BARCELONA = 'BAR'
	ATLETICO MADRID = 'ATL'
	MANCHESTER CITY = 'MCY'
	CHELSEA = 'CHE'
	ARSENAL = 'ARS'
	LIVERPOOL = 'LIV'
	MANCHESTER UNITED = 'MNU'
	TOTTENHAM = 'TOT'
	PSG = 'PSG'
	OLYMPIQUE LYONNAISE = 'OL'
	AC MILAN = 'MIL'
	JUVENTUS = 'JUV'
	INTER MILAN = 'INT'
	NAPOLI = 'NAP'
	ROMA = 'ROMA'
	BAYERN MUNICH = 'BMU'
	BORRUSIA DORTMUND = 'BOR'

	REGION_CHOICES = (
		(REAL MADRID = 'Real Madrid'),
		(BARCELONA = 'Barcelona'),
		(ATLETICO MADRID = 'Atletico Madrid'),
		(MANCHESTER CITY = 'Manchester City'),
		(CHELSEA = 'Cheslea'),
		(ARSENAL = 'Arsenal'),
		(LIVERPOOL = 'Liverpool'),
		(MANCHESTER UNITED = 'Manchester United'),
		(TOTTENHAM = 'Tottenham Hotspur'),
		(PSG = 'Paris St. Germain'),
		(OLYMPIQUE LYONNAISE = 'Lyon'),
		(AC MILAN = 'AC Milan'),
		(JUVENTUS = 'Juventus'),
		(INTER MILAN = 'Inter Milan'),
		(NAPOLI = 'Napoli'),
		(ROMA = 'Roma'),
		(BAYERN MUNICH = 'Bayern Munich'),
		(BORRUSIA DORTMUND = 'Borussia Dortmund'),
	)
	soccer_region = models.CharField(max_length=2, choices=REGION_CHOICES, default=NORTH_AMERICA)
