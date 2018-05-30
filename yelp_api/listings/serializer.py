from rest_framework import serializers
from .models import Listing

class YelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing