import graphene
import dao_mission
import json  

#description of API
class Mission(graphene.ObjectType):
    id = graphene.Int()
    missionName = graphene.String()
    triggerTime = graphene.String()
    
class AddMission(graphene.Mutation):
    class Arguments:
        missionName = graphene.String()
        triggerTime = graphene.String()
    status = graphene.String()
    mission = graphene.Field(Mission)
    def mutate(self, info, missionName, triggerTime):
        print("mutate(): get missionName:%s, triggerTime%s" % (missionName, triggerTime))
        if dao_mission.add_mission(missionName, triggerTime):
            status = "success"
        else:
            status = "fail"
        mission = Mission(id=0, missionName=missionName, triggerTime=triggerTime)
        return AddMission(mission=mission, status=status)
    
class DeleteMission(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
    status = graphene.String()
    mission = graphene.Field(Mission)
    def mutate(self, info, id):
        print("mutate(): delete mission id: %d" % (id))
        (id, mission_name, trigger_time, operation_status) = dao_mission.delete_mission(id)
        if operation_status:
            status = "success"
        else:
            status = "fail"
        mission = Mission(id=id, missionName=mission_name, triggerTime=trigger_time)
        return DeleteMission(mission=mission, status=status)

class ModifyMission(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        missionName = graphene.String()
        triggerTime = graphene.String()
    status = graphene.String()
    mission = graphene.Field(Mission)
    def mutate(self, info, id, missionName, triggerTime):
        print("mutate(): modify mission id: %d" % (id))
        (id, mission_name, trigger_time, operation_status) = dao_mission.modify_mission(id, missionName, triggerTime)
        if operation_status:
            status = "success"
        else:
            status = "fail"
        mission = Mission(id=id, missionName=mission_name, triggerTime=trigger_time)
        return ModifyMission(mission=mission, status=status)

class Mutations(graphene.ObjectType):
    addMission = AddMission.Field()
    deleteMission = DeleteMission.Field()
    modifyMission = ModifyMission.Field()
    

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

schema = graphene.Schema(query=Query, mutation=Mutations)
