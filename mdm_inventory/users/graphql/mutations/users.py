# django
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist, ValidationError

# graphene
import graphene
import graphql_jwt


# types
from mdm_inventory.users.graphql.types import UserType

# utils
from mdm_inventory.utils.graphql.generic_mutation import GenericMutationSerializer


class InputUserData(graphene.InputObjectType):
    first_name = graphene.String(description="first name")
    last_name = graphene.String(description="last name")
    email = graphene.String(description="correo electronico")
    username = graphene.String(description="Nombre de usuario")
    profile_picture = graphene.String(description="Foto de perfil")
