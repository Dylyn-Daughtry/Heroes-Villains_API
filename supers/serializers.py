from rest_framework import serializers
from .models import Super

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'super_type_id', 'alter_ego', 'catchphrase', 'name', 'primary_ability', 'secondary_ability']