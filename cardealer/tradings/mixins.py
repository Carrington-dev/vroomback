from rest_framework import mixins, viewsets
class VehicleMixin(mixins.ListModelMixin, \
        mixins.RetrieveModelMixin, \
        viewsets.GenericViewSet):
    pass