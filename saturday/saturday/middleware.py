import graphene
import dao_mission
import json  
import logging

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
        logging.info("add: missionName: %s, triggerTime: %s" % (missionName, triggerTime))
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
        logging.info("delete: mission id: %d" % (id))
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
        logging.info("modify:  mission id: %d, mission_name: %s, trigger_time: %s" % (id, mission_name, trigger_time))
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
    #if there is argument "id", that only use id to query, ignore mission_name and trigger_time field
    #if the argument "id" equal 0, then use mission_name or trigger_time to query
    #otherwise, query all mission
    missions = graphene.List(Mission, 
                             id = graphene.Int(required=False, default_value=0),
                             mission_name = graphene.String(required=False, default_value="null"),
                             trigger_time = graphene.String(required=False, default_value="null"))
    def resolve_missions(self, info, id, mission_name, trigger_time):
        if id != 0:
            logging.info("query: by id: %d" % (id))
            results = dao_mission.query_mission_by_id(id)
        elif mission_name!="null" or trigger_time!="null":
            logging.info("query: by str: mission_name: %s, trigger_time: %s" % (mission_name, trigger_time))
            results = dao_mission.query_mission_by_mission_name_and_trigger_time(mission_name, trigger_time)
        else:
            logging.info("query: by default")
            results = dao_mission.query_mission_by_id(0)
        m = []
        for row in results:
            id = row[0]
            mission_name = row[1]
            trigger_time = row[2]
            m.append(Mission(id=row[0], missionName=row[1], triggerTime=row[2]))
        m1 = graphene.List(Mission)
        m1 = m
        return m1

    
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
