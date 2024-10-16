from source.settings import *
from source.data_structures import BSPNode

class BSPTreeTraverser:
    def __init__(self, engine):
        self.engine = engine
        self.root = engine.bsp_builder.root
        self.segments = engine.bsp_builder.segments

    def update(self):
        pass

    def traverse(self, node: BSPNode):
        pass