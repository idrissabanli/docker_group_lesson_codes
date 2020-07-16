from rest_framework import serializers
from stories.models import Recipe, Category, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'title',
        )



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'image',
        )


class RecipeReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'image',
            'slug',
            'author',
            'tags',
            'category',
            'short_description',
            'long_description',
            'created_at',
            'updated_at',
        )


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'image',
            'slug',
            'author',
            'tags',
            'category',
            'short_description',
            'long_description',
            'created_at',
            'updated_at',
        )


