from rest_framework import serializers
from .models import TipPrediction

class TipPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipPrediction
        fields = '__all__'