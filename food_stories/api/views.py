from django.shortcuts import render, get_object_or_404
from stories.models import Recipe
from api.serializers import RecipeSerializer, RecipeReadSerializer, SubscriberSerializer
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, MethodNotAllowed
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import BasicAuthentication
from api.utils import CsrfExemptSessionAuthentication

def login_required(f):
    def wrapper(*args, **kwargs):
        request = args[0]
        if not request.user.is_authenticated:
            raise PermissionDenied
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT


@api_view(http_method_names=('GET', 'POST',))
def recipes_api(request):
    if request.method == 'GET':
        recipes = Recipe.objects.filter(is_published=True)
        serializer = RecipeReadSerializer(recipes, context={'request': request}, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    if not request.user.is_authenticated:
        raise PermissionDenied
    elif request.method == 'POST':
        recipe_data = request.data
        serializer = RecipeSerializer(data=recipe_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    else:
        raise MethodNotAllowed


@api_view(('GET', 'PUT', 'PATCH', 'DELETE'))
@login_required
def recipe(request, id):
    response_data = {
        'message': 'success',
        'action': 'read'
    }
    status_code = HTTP_200_OK
    if request.method == 'GET':
        recipe = get_object_or_404(Recipe, id=id) #Recipe.objects.get(id=id, )
        serializer = RecipeReadSerializer(recipe)
        response_data['recipe'] = serializer.data
    elif request.method == 'PUT':
        recipe = get_object_or_404(Recipe, id=id)
        serializer = RecipeSerializer(recipe, context={'request': request}, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data['recipe'] = serializer.data
        response_data['action'] = 'modify'
    elif request.method == 'PATCH':
        recipe = get_object_or_404(Recipe, id=id)
        serializer = RecipeSerializer(instance=recipe, context={'request': request}, data=request.data, partial=True, )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data['recipe'] = serializer.data
        response_data['action'] = 'partial_modify'
    elif request.method == 'DELETE':
        recipe = get_object_or_404(Recipe, id=id)
        recipe.delete()
        response_data = {}
        status_code = HTTP_204_NO_CONTENT
    return Response(response_data, status=status_code)


class SubscriberCreateAPIView(CreateAPIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    serializer_class = SubscriberSerializer
