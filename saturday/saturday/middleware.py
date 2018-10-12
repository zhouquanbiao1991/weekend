import graphene
import dao_mission
import json  

#description of API
class Mission(graphene.ObjectType):
    id = graphene.Int()
    missionName = graphene.String()
    triggerTime = graphene.String()

class addMission(graphene.Mutation):
    class Arguments:
        missionName = graphene.String()
        triggerTime = graphene.String()
    mission = graphene.Field(Mission)
    status = graphene.String()
    def mutate(self, info, missionName, triggerTime):
        print("mutate(): get missionName:%s, triggerTime%s" % (missionName, triggerTime))
        if dao_mission.add_mission(mission_name, trigger_time):
            status = "success"
        else:
            status = "fail"
        mission = Mission(missionName=missionName, triggerTime=triggerTime)
        return addMission(mission=mission, status=status)

class Mutation(graphene.ObjectType):
    add = graphene.Field(addMission)
    #deleteMission = 
    #modifyMission = 
    pass

class Query(graphene.ObjectType):
    mission = graphene.Field(Mission, id = graphene.Int(required=False))
    def resolve_mission(self, info, id):
        print("goto sql query")
        results = dao_mission.query_mission(id)
        m = graphene.Field(Mission)
        for row in results:
            id = row[0]
            mission_name = row[1]
            trigger_time = row[2]
            #m.append(Mission(id=row[0], missionName=row[1], triggerTime=row[2]))
            return Mission(id=row[0], missionName=row[1], triggerTime=row[2])
        return m
    
def request(graphene_str):
    print("graphene request: " + graphene_str)
    result = schema.execute(graphene_str)
    print("result.data : ")
    print(result.data)

    metadata = json.dumps(result.data)
    print("metadata : ")
    print(metadata)
    return metadata

schema = graphene.Schema(query=Query, mutation=Mutation)
