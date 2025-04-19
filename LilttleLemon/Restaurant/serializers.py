from rest_framework import serializers
from django.contrib.auth.models import User

class userSerializers(serializers.ModelSerializer):
    class Meta:
        Model=User
        fields = ['url', 'username', 'email', 'groups']