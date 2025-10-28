from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','due_date','completed','created_at','updated_at']

from django.contrib.auth.models import User
from rest_framework import serializers

class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        user, created = User.objects.get_or_create(
            username=email,
            defaults={"email": email},
        )
        if created:
            user.set_password(password)
            user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
