import asyncio
from abc import ABC

import threading

import tornado.web
import tornado.ioloop


class PingRequestHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        print("200 OK")
        self.set_status(200)
        self.flush()


class ServerThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(ServerThread, self).__init__(*args, **kwargs)
        self.app = None
        self.http_server = None

    def run(self):
        asyncio.set_event_loop(asyncio.new_event_loop())

        self.app = tornado.web.Application([(r"/", PingRequestHandler), ])
        self.http_server = self.app.listen(3050)
        tornado.ioloop.IOLoop.current().start()

    def stop(self):
        tornado.ioloop.IOLoop.current().stop()
        self.http_server.stop()
        exit(0)
