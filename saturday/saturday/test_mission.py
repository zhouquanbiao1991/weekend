import unittest
import random
import middleware
import json

# test curl :
# query_str: curl localhost:8888/ -X POST -d "query myQuery { missions(id : 2) { id, missionName, triggerTime } }"
# add_str: curl localhost:8888/ -X POST -d "mutation myMutation { addMission(missionName: \"hurryup\", triggerTime: \"anytime\") { mission { id } status } }"
# del_str: curl localhost:8888/ -X POST -d "mutation mydelMutation { deleteMission(id: 3) { mission { id missionName triggerTime } status } }"
# modify_str: curl localhost:8888/ -X POST -d "mutation mymodifyMutation { modifyMission(id: 6, missionName: \"gogogo\", triggerTime: \"wait for what\") { mission { id missionName triggerTime } status } }"

class TestMission(unittest.TestCase):
    def insert_test(self, test_string):
        #insert
        insert_str = "mutation myMutation { addMission(missionName: \"%s\", triggerTime: \"%s\") { mission { id missionName triggerTime } status } }" % (test_string, test_string)
        result = middleware.request(insert_str)
        result_json = json.loads(result)
        self.assertEqual(result_json['addMission']["status"], "success")
        self.assertEqual(result_json['addMission']["mission"]["missionName"], test_string)
        self.assertEqual(result_json['addMission']["mission"]["triggerTime"], test_string)
    
    def query_by_missionName_and_triggerTime_test(self, test_string):
        query_str = "query myQuery { missions(missionName: \"%s\", triggerTime: \"%s\") { id, missionName, triggerTime } }" \
            % (test_string, test_string)
        result = middleware.request(query_str)
        result_json = json.loads(result)
        print(result_json)
        self.assertEqual(result_json['missions'][0]['missionName'], test_string)
        self.assertEqual(result_json['missions'][0]['triggerTime'], test_string)
        return result_json['missions'][0]["id"]
    
    def query_by_id_test(self, id, string):
        query_str = "query myQuery { missions(id: %d) { id, missionName, triggerTime } }" % id
        result = middleware.request(query_str)
        result_json = json.loads(result)
        self.assertEqual(result_json['missions'][0]["missionName"], string)
        self.assertEqual(result_json['missions'][0]['triggerTime'], string)

    def modify_test(self, id, modify_test_string):
        modify_query = "mutation mymodifyMutation { modifyMission(id: %d, missionName: \"%s\", triggerTime: \"%s\") { mission { id missionName triggerTime } status } }"\
           % (id, modify_test_string, modify_test_string)
        result = middleware.request(modify_query)
        result_json = json.loads(result)
        self.assertEqual(result_json['modifyMission']['status'], "success")

    def del_test(self, id):
        del_str = "mutation mydelMutation { deleteMission(id: %d) { mission { id missionName triggerTime } status } }" % id
        result = middleware.request(del_str)
        result_json = json.loads(result)
        self.assertEqual(result_json['deleteMission']['status'], "success")

    def test_all(self):
        while(1):
            test_string = "test_string" + str(random.randint(0,100))
            query_str = "query myQuery { missions(missionName: \"%s\", triggerTime: \"%s\") { id, missionName, triggerTime } }" % (test_string, test_string)
            result = middleware.request(query_str)
            result_python = json.loads(result)
            if result_python['missions'] == []:
                break
        TestMission.insert_test(self, test_string)
        id = TestMission.query_by_missionName_and_triggerTime_test(self, test_string)
        TestMission.query_by_id_test(self, id, test_string)

        #modify
        while(1):
            modify_test_string = "modify_test_string" + str(random.randint(0,100))
            query_str = "query myQuery { missions(missionName: \"%s\", triggerTime: \"%s\") { id, missionName, triggerTime } }" \
                % (modify_test_string, modify_test_string)
            result = middleware.request(query_str)
            result_python = json.loads(result)
            if result_python['missions'] == []:
                break
        TestMission.modify_test(self, id, modify_test_string)
        TestMission.query_by_id_test(self, id, modify_test_string)
        TestMission.del_test(self, id)

        #query fail
        query_str = "query myQuery { missions(id: %d) { id, missionName, triggerTime } }" % id
        result = middleware.request(query_str)
        result_json = json.loads(result)
        self.assertEqual(result_json['missions'], [])

if __name__ == '__main__':
    unittest.main()

