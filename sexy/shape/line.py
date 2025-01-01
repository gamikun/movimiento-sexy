from wand.color import Color
from math import sqrt

class Line:
    def __init__(self, xy1, xy2):
        self.xy1 = xy1
        self.xy2 = xy2
        self.opacity = 1.0
        
        self.appear_frame = 0

    def draw(self,
        context=None,
        image=None,
        time=1.0,
        color=Color('black'),
        linearity='quadratic'
    ):
        assert context
        x1, y1 = self.xy1
        x2, y2 = self.xy2

        w = x2 - x1
        h = y2 - y1

        #if linearity == 'quadratic':
        #    time = sqrt(time)

        context.line(
            (x1, y1),
            (x1 + w * time, y1 + h * time)
        )

        context(image)