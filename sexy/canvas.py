from sexy import Linearity


class Canvas:
    def __init__(self, context):
        self.context = context

    def line(self, src, dst,
        time=1.0,
        linearity=Linearity.LINEAL
    ):
        x, y = src
        subx, suby = dst
        w = subx - x
        h = suby - y

        self.context.move_to(*xy1)
        self.context.line_to(
            x + w * time,
            y + h * time
        )