from tastypie.resources import ModelResource
from apppet.models import Status,Animal,Register


class StatusResource(ModelResource):
    class Meta:
        queryset = Status.objects.all()
        resource_name = 'status'
class AnimalResource(ModelResource):
    class Meta:
        queryset = Animal.objects.all()
        resource_name = 'animals'
class RegisterResource(ModelResource):
    class Meta:
        queryset = Register.objects.all()
        resource_name = 'users'

