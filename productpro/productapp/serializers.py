from rest_framework import serializers
from .models import product
class productserializers(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=["id","location","farm","product","quantity","price"]