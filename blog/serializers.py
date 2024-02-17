# blog/serializers.py
from rest_framework import serializers
from .models import Article, EditorProfile


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class EditorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditorProfile
        fields = '__all__'
