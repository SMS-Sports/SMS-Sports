from django.shortcuts import render_to_response
from django.template import RequestContext
from subscribe.models import Region, NATeam, EUTeam

# Create your views here.
def index(request):
    region = Region.objects.all
    nateam = NATeam.objects.all
    euteam = EUTeam.objects.all
    return render_to_response('subscribe.html', {'region': region, 'nateam': nateam, 'euteam': euteam})