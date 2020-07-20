from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from stories.models import Story
from api.serializers import StorySerializer, StoryReadSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class StoryModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Story.objects.filter(is_published=True)
    # serializer_class = StorySerializer
    serializer_classes = {
        'default': StorySerializer,
        'create': StorySerializer,
        'update': StorySerializer,
        'partial_update': StorySerializer,
        'delete': StorySerializer,
        'list': StoryReadSerializer,
        'retrieve': StoryReadSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_classes.get('default'))