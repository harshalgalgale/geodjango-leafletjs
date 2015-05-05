from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string

from waypoints.models import WayPoint


def index(request):
	'Display map'
	waypoints = WayPoint.objects.order_by('name')
	return render_to_response('waypoints/index.html', {
		'title': 'Waypoints Tutorial',
		'waypoints': waypoints,
		'content': render_to_string('waypoints/waypoints.html', {'waypoints': waypoints})
		})

def waypoints(request):
	return HttpResponse('Hello')

def search(request):
	return HttpResponse('Hello')

def search_near_roads(request):
	return HttpResponse('Hello')