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
	if request.method == 'POST':
		data = request.POST.get('content')
		if data:
			data = json.loads(data)
			for wp_json in data:
				waypoint = WayPoint.objects.get(id=int(wp_json['id']))
				waypoint.geometry.set_x(float(wp_json['x']))
				waypoint.geometry.set_y(float(wp_json['y']))
				waypoint.save()
			return HttpResponse(json.dumps({'isOk': 1}), mimetype='application/json')
		else:
			return HttpResponse(json.dumps({'isOk': 0, 'message': 'No data to save.'}))
	return HttpResponse('Hello')

def search(request):
	return HttpResponse('Hello')

def search_near_roads(request):
	return HttpResponse('Hello')