import middleware
import tornado.ioloop
import tornado.web
import logging

listen_port = 8889

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    def post(self):
        request_body_bytes = self.request.body
        request_str = str(request_body_bytes,'utf-8')
        logging.info("receive a post request: %s", request_str)
        result_str = middleware.request(request_str)
        logging.info("request result: %s", result_str)
        result_bytes = result_str.encode('utf-8')
        self.write(result_bytes)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s", filename="saturday.log", level=logging.DEBUG)
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(listen_port, address="0.0.0.0")
    logging.info("listen to %d", listen_port)
    tornado.ioloop.IOLoop.current().start()

