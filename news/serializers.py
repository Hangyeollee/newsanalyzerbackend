from rest_framework import serializers
from .models import SwedishWords


class SwedishwordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwedishWords
        fields = ("word", "count")
