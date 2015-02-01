from django.contrib import admin
from subscribe.models import Region
from subscribe.models import NATeam
from subscribe.models import EUTeam

# Register your models here.
admin.site.register(Region)
admin.site.register(NATeam)
admin.site.register(EUTeam)