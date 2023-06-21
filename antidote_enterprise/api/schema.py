import graphene
from graphene_django.types import DjangoObjectType
from .models import Provider


class ProviderType(DjangoObjectType):
    class Meta:
        model = Provider


class Query(graphene.ObjectType):
    all_providers = graphene.List(ProviderType)
    provider = graphene.Field(ProviderType, id=graphene.Int())

    def resolve_all_providers(self, info, **kwargs):
        return Provider.objects.all()

    def resolve_provider(self, info, **kwargs):
        identifier = kwargs.get('id')

        if id is not None:
            Provider.objects.get(pk=identifier)

        return None
