from rest_framework import serializers
from stories.models import Recipe, Category, Tag, Story

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
    author = serializers.PrimaryKeyRelatedField(read_only=True)

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
    
    def validate(self, data):
        request = self.context.get('request')
        data['author'] = request.user
        return super().validate(data)


class StoryReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Story
        fields = (
            'id',
            'title',
            'image',
            'slug',
            'author',
            'tags',
            'category',
            'long_description',
            'created_at',
            'updated_at',
        )


class StorySerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Story
        fields = (
            'id',
            'title',
            'image',
            'slug',
            'author',
            'tags',
            'category',
            'long_description',
            'created_at',
            'updated_at',
        )
    
    def validate(self, data):
        request = self.context.get('request')
        data['author'] = request.user
        return super().validate(data)


