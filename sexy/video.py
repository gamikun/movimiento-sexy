from PIL import Image
from wand.drawing import Drawing
from wand.image import Image as WandImage
from wand.color import Color
import subprocess
try:
    import cairo
except ModuleNotFoundError:
    class cairo:
        ImageSurface = None
import PIL


class VideoEncoder:
    def __init__(self, framerate=30, filename=None, image_format='png'):
        self.framerate = framerate
        self.filename = filename
        self.p = None
        self.do_pipe = True
        self.image_format = image_format
        self.process = None

    def start(self):
        do_pipe = dict(
            #stdout=subprocess.PIPE,
            #stderr=subprocess.PIPE,
        ) if self.do_pipe else {}

        self.process = subprocess.Popen(
            ['ffmpeg',
                '-f', 'image2pipe',
                '-framerate', str(self.framerate),
                '-probesize', '20M',
                '-vcodec', self.image_format,
                '-i', '-',
                '-c:v', 'libx264',
                '-pix_fmt', 'yuv420p',
                # '-crf', '26',
                '-preset', 'ultrafast',
                '-an',
                '-f', 'mp4',
                '-s', '1920x1080',
                #'-r', str(self.framerate),
                #'-b:v', '100k',
                '-y',
                self.filename
            ],
            stdin=subprocess.PIPE,
            **do_pipe,
        )

    def append_frame(self, frame, size=None):
        """if isinstance(frame, cairo.ImageSurface):
            frame.write_to_png(self.process.stdin)"""
        if isinstance(frame, PIL.Image.Image):
            frame.save(self.process.stdin, self.image_format)
        elif isinstance(frame, bytes):
            img = Image.frombytes('RGBA', (1920, 1080), frame)
            img.save(self.process.stdin, 'png')
        else:
            raise TypeError("Invalida frame type")

    def finalize(self):
        self.process.communicate()
