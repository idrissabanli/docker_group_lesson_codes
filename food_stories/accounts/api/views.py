from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.api.serializers import RegisterSerializer, UserProfileSerializer, LoginSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView


@api_view(('POST',))
def register(request):
    user_data = request.data
    serializer = RegisterSerializer(data=user_data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=HTTP_201_CREATED)


class CustomAuthToken(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        user_serializer = UserProfileSerializer(user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_detail': user_serializer.data
        })
