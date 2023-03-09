from rest_framework import serializers

from .models import Article, Author


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    surname = serializers.CharField(max_length=255)
    group = serializers.CharField(max_length=255)
    money = serializers.IntegerField()



class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    reason = serializers.CharField(max_length=120)
    details = serializers.CharField(max_length=255)

    author_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Article.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.reason = validated_data.get('reason', instance.reason)
        instance.details = validated_data.get('details', instance.details)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.save()
        return instance

    