from waypoints.models import WayPoint
from django.contrib.gis import admin


admin.site.register(WayPoint, admin.GeoModelAdmin)
