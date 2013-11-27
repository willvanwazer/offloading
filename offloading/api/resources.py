from tastypie.resources import ModelResource
from tastypie.api import Api
from offloading.api.models import Station, Confirmation, Incident, Tweet
from tastypie import fields


class StationResource(ModelResource):
    class Meta:
        queryset = Station.objects.all()
        allowed_methods = ['get']

class IncidentResource(ModelResource):
    station = fields.ForeignKey(StationResource, 'station', full=True)
    
    class Meta:
        queryset = Incident.objects.all()
        allowed_methods = ['get']
        
        
v1_api = Api(api_name='v1')
v1_api.register(StationResource())
v1_api.register(IncidentResource())