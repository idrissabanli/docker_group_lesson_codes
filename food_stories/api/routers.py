from rest_framework.routers import DefaultRouter

from api.viewsets import StoryModelViewSet

router = DefaultRouter()

router.register(r'stories', StoryModelViewSet)
