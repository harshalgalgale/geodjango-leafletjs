from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	'Display map'
	return render_to_response('waypoints/index.html', {
		'title': 'Waypoints Tutorial'
		})

def waypoints(request):
	return HttpResponse('Hello')

def search(request):
	return HttpResponse('Hello')

def search_near_roads(request):
	return HttpResponse('Hello')