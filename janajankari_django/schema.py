import graphene

from apps import inventory
import apps.inventory.schema


class Query(inventory.schema.Query, graphene.ObjectType):
    # This class extends all abstract apps level Queries and graphene.ObjectType
    pass


schema = graphene.Schema(query=Query)