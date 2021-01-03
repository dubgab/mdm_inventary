import graphene

# Querys
from mdm_inventory.users.graphql.query import QueryUserGeneric

#Mutations
from mdm_inventory.users.graphql.mutation import MutationGenericUsers

class Query(
        QueryUserGeneric,
        graphene.ObjectType
):
    pass

class Mutation(
    MutationGenericUsers,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query , mutation=Mutation )
