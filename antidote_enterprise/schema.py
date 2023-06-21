import antidote_enterprise.api.schema
import graphene


class Query(antidote_enterprise.api.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
