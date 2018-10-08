import graphene

class Query_obj(graphene.ObjectType):
    hell = graphene.String(name = graphene.String(default_value="stranger"))

    def resolve_hell(self, info, name):
        return "ni hao" + name

schema = graphene.Schema(query=Query_obj)
result = schema.execute("{hell}")
print(result.data["hell"])



