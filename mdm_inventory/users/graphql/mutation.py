#graphql
import graphene
from graphene_django.types import DjangoObjectType, ObjectType
import graphql_jwt

#mutations
from mdm_inventory.users.graphql.mutations import (CreateClient)

class MutationGenericUsers(graphene.ObjectType):
    create_client = CreateClient.Field()