from sexy.server import RenderServer
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-front', dest='front', default='')
args = parser.parse_args()

RenderServer(
    image_format='png',
    front_path=args.front
).serve()