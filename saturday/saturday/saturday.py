import middleware
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    def post(self):
        request_body_bytes = self.request.body
        self.write(request_body_bytes)

        query_str = str(request_body_bytes,'utf-8')
        str1 = middleware.request(query_str)
        print("type: "+type(str1).__name__)
        b = str1.encode('utf-8')
        self.write(b)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

# test curl :
# query_str = curl localhost:8888/ -X POST -d "query myQuery { mission(id : 2) { id, missionName, triggerTime } }"
# query_str = curl localhost:8888/ -X POST -d "mutation myMutation { add(missionName: "hurryup", triggerTime:"anytime") { mission { id }, status } }"
# query_str = mutation myFirstMutation { createPerson(name:"Peter") { person { name } ok } }
