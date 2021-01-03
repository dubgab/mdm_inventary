# Django
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import (
    FieldDoesNotExist, ImproperlyConfigured, ValidationError,
)

# DRF
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#models

from mdm_inventory.users.models import Client

class CreateClientSerializer(serializers.ModelSerializer):
    """Cient create serializer"""
    class Meta:
        model = Client
        fields = (
            'id',
            'first_name',
            'last_name',
            'dni',
            'phone_number',
            'full_name',
            'address',
        )
    
    def validate(self, data):
        return data

    def create(self, data):
        client = Client.objects.create(**data)
        return client