import graphene
import datetime

class Query_obj(graphene.ObjectType):
   # normal_val = ' who r u '
    first = graphene.String()

    sec = graphene.String(sec_val = graphene.String(default_value="stranger"))
    
    third_val = graphene.String(default_value="stranger")    
    third = graphene.String(third_val)

    hell = graphene.String()
    episode = graphene.Enum('episode', [('a',1), ('b',2), ('c',3)])
    
    def resolve_first(self, info):
        return "first"
    def resolve_sec(self, info, sec_val):
        return "sec" + sec_val
    def resolve_third(self, info, sec_val):
        return "third" + sec_val

schema = graphene.Schema(query=Query_obj)
result1 = schema.execute("{first}")
#result2 = schema.execute("{sec}")
#result3 = schema.execute("{third}")
print(result.data["first"])
#print(result.data["sec"])
#print(result.data["third"])



