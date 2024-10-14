from settings import *
from data_structures import *
from levels.level_0 import *

class LevelData:
    def __init__(self, engine):
        self.engine = engine

        self.raw_segments = [Segment(p0, p1) for (p0, p1) in SEGMENTS]
