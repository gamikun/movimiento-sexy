from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, StaticFileHandler
from sexy.video import VideoEncoder
from binascii import hexlify
from os import urandom
import json


class State:
    encoder = None


class RenderServer:
    def __init__(self, image_format='png', front_path=''):
        self.loop = IOLoop.current()
        self.app = Application([
            (r'/control', ControlHandler),
            (r'/(.*)', StaticFileHandler, {"path": front_path})
        ],
            image_format=image_format
        )

    def serve(self):
        self.app.listen(4225)
        self.loop.start()


class FrontHandler(RequestHandler):
    def initialize(self, front_filename=''):
        self.front_filename = front_filename

    def get(self):
        self.write(open(self.front_filename, 'rb').read())


class ControlHandler(RequestHandler):
    def post(self):
        if State.encoder is not None:
            self.write('')
            return

        settings = self.application.settings

        State.encoder = VideoEncoder(
            filename='algo.mp4',
            image_format=settings.get('image_format', 'png'),
        )
        State.encoder.start()

        print('Render started')

        self.write('')

    def put(self):
        frame = self.request.files['frame'][0]
        State.encoder.append_frame(frame['body'])
        self.write('que')

    def delete(self):
        if State.encoder:
            State.encoder.finalize()
            State.encoder = None
            print('Render killed')
        
        self.write('')
