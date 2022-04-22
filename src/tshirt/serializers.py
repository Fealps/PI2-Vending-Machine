
from rest_framework import serializers
from .models import Tshirt

class TshirtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tshirt
        fields = '__all__'