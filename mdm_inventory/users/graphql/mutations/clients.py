# python
import jwt

# django
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist, ValidationError

# graphene
import graphene
import graphql_jwt

# Auth
from graphql_jwt.decorators import login_required

# models
from mdm_inventory.users.models import Client

# serializers
from mdm_inventory.users.serializers import CreateClientSerializer

# types
from mdm_inventory.users.graphql.types import ClientType

# utils
from mdm_inventory.utils.graphql.generic_mutation import GenericMutationSerializer

class InputClientData(graphene.InputObjectType):
    first_name  = graphene.String(description="first name")
    last_name= graphene.String(description="last name")
    dni = graphene.String(description="DNI")
    phone_number = graphene.String(description="phone number")
    full_name  = graphene.String(description="full name")
    address = graphene.Int(description="ID address relate" , required=False)

class CreateClient(GenericMutationSerializer):

    class Arguments:
        input = InputClientData(description="Input user data")

    client = graphene.Field(ClientType)

    class Meta:
        model: Client
        description = 'CreateClient in data base'
        serializer_class = CreateClientSerializer

    @classmethod
    def mutate(cls, root, info, **kwargs):
        client, message, status = cls.perform_mutation(root, info, **kwargs)
        message = _("Cliente Agregado")
        return cls(client=client, message=str(message), status=status)
