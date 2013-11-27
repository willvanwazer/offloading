from tastypie.resources import ModelResource
from offloading.api.models import Station, Confirmation, Incident, Tweet

# class StationResource(ModelResource):

class IncidentResource(ModelResource):
    class Meta:
        queryset = Incident.objects.all()
        allowed_methods = ['get']