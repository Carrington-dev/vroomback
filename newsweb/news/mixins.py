from rest_framework import mixins, viewsets

class PostCreateReadMixin(viewsets.GenericViewSet. mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    pass