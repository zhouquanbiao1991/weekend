
import graphene

################ simple ##################
class Query_simple(graphene.ObjectType):
    last = graphene.String(las=graphene.String(default_value="stranger"))
    def resolve_last(self, info, las):
        return las
schema = graphene.Schema(query=Query_simple)
result = schema.execute("{last}")
print(result.data["last"])


################ interface ##################
class Character(graphene.Interface):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    friends = graphene.List(lambda: Character)

class Human(graphene.ObjectType):
    class Meta:
        interfaces = (Character, )

    #starships = graphene.List(Starship)
    home_planet = graphene.String()

class Droid(graphene.ObjectType):
    class Meta:
        interfaces = (Character, )

    primary_function = graphene.String()
    
class Query_interface(graphene.ObjectType):
    hero = graphene.Field(
        Character,
        required=True,
        episode=graphene.Int(required=True)
    )

    def resolve_hero(self, info, episode):
        # Luke is the hero of Episode V
        if episode == 5:
        #    return get_human(name='Luke Skywalker')
            return 'Luke Skywalker'
        #return get_droid(name='R2-D2')
        return 'R2-D2'
    
schema = graphene.Schema(query=Query_interface, types=[Human, Droid])
query_str = """
query {
    hero(episode: 5 ) {
        __typename
        name
        ... on Droid {
            primaryFunction
        }
        ... on Human {
            homePlanet
        }
    }
}
"""
result = schema.execute(query_str)
print(result.data)


################ mutation ################
class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()

class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String()
    ok = graphene.Boolean()
    person = graphene.Field(Person)
    def mutate(self, info, name):
        person = Person(name=name)
        ok = True
        return CreatePerson(person=person, ok=ok)

class Query_mutation(graphene.ObjectType):
    person = graphene.Field(Person)

class Mutations(graphene.ObjectType):
    create_person = CreatePerson.Field()

schema = graphene.Schema(query=Query_mutation, mutation=Mutations)
query_str = """
mutation myFirstMutation {
    createPerson(name:"Peter") {
        person {
            name
        }
        ok
    }
}
"""
result = schema.execute(query_str)
print(result.data["createPerson"])

################ github_example ################
class Patron(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()
    
class Query(graphene.ObjectType):
    patron = graphene.Field(Patron)
    def resolve_patron(self, info):
        return Patron(id=1,name="abc",age=19)

schema = graphene.Schema(query=Query)
query = """
    query something{
      patron {
        id
        name
        age
      }
    }
"""
result = schema.execute(query)
#result = schema.execute('query { patron {id} }')
print("obj: ")
print(result.data)

################ variable ################
class Patron(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()
    
class Query_variable(graphene.ObjectType):
    patron = graphene.Field(Patron, age=graphene.Int(required=False))
    def resolve_patron(self, info, age):
        if age == 1:
            return Patron(id=1,name="abc",age=19)
        else:
            return Patron(id=2,name="222",age=22)

schema = graphene.Schema(query=Query_variable)
query_str = """
    query something{
      patron (age : 3){
        id
        name
        age
      }
    }
"""
result = schema.execute(query_str)
print(result.data['patron'])



