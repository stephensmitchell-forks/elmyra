"""Renders and exports all visualizations, over and over"""

from glob import glob
from os import path
from subprocess import call

from configuration import BLENDER_PATH


RENDER_SCRIPT = path.join(path.dirname(__file__), 'blender_render.py')
LOOP = True


def render(id):
    call([
        BLENDER_PATH,
        "--background",
        "--python", RENDER_SCRIPT,
        "--",
        "--id", id,
        "--device", "GPU"
    ])


while True:
    for viz in glob("visualizations/*"):
        id = path.basename(viz)
        render(id)

    if not LOOP:
        break
