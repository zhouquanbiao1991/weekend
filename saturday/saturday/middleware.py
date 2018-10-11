import graphene
import dao_mission

#description of API
class Mission(graphene.ObjectType):
    id = graphene.Int();
    mission_name = graphene.String();
    trigger_time = graphene.String();

class Query(graphene.ObjectType):
    mission = graphene.Field(Mission, 
                             id = graphene.Int(), 
                             mission_name = graphene.String(), 
                             trigger_time = graphene.String())
    
    def resolve_mission(self, info, id, mission_name, trigger_time):
        
        results = dao_mission.query_mission(id)
        for row in results:
            id = row[0]
            mission_name = row[1]
            trigger_time = row[2]
        return Mission(results)

schema = graphene.Schema(query=Query)
def request():
    result = schema.execute("{mission}")
    print(result.data["mission"])


