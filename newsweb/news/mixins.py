from rest_framework import mixins, viewsets

class PostListReadMixin(mixins.ListModelMixin, \
        mixins.RetrieveModelMixin, \
        viewsets.GenericViewSet):
    pass