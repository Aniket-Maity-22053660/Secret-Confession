from rest_framework import serializers
from .models import User, Confession, Reaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'reputation', 'created_at']

class ConfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confession
        fields = [
            'id', 'anonymous_name', 'content', 'category',
            'latitude', 'longitude', 'reactions_count',
            'created_at', 'expires_at'
        ]

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['id', 'type', 'confession', 'user', 'created_at']
