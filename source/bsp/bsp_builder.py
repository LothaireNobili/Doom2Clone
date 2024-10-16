from source.settings import *
from source.data_structures import Segment, BSPNode
from source.utils import cross_2d
from copy import copy

class BSPTreeBuilder:
    def __init__(self, engine):
        self.engine = engine
        self.raw_segments = self.engine.level_data.raw_segments

        self.root = BSPNode()

        self.segments = []  # segments created during BSP tree creation
        self.seg_id = 0

        self.build(self.root, self.raw_segments)

    def split_space(self, node:BSPNode, segments:Segment):
        splitter_segment = segments[0]
        splitter_pos = splitter_segment.pos
        splitter_vec = splitter_segment.vector

        node.splitter_vec = splitter_vec
        node.splitter_p0 = splitter_pos[0]
        node.splitter_p1 = splitter_pos[1]

        front_segment, back_segment = [], []

        for segment in segments[1:]:
            segment_start, segment_end = segment.pos[0], segment.pos[1]
            segment_vector = segment.vector

            numerator = cross_2d(segment_start - splitter_pos[0], splitter_vec) 
            denominator = cross_2d(segment_vector, splitter_vec)

            denominator_is_zero = abs(denominator) < EPSILON #if denominator is zero, the segment is parallel to the splitter

            numerator_is_zero = abs(numerator) < EPSILON #if numerator is zero, the segment and the splitter are collinear

            if denominator_is_zero and numerator_is_zero:
                front_segment.append(segment)
                continue
            
            if not denominator_is_zero:
                intersection = numerator / denominator

                if 0.0 < intersection < 1.0:
                    
                    intersection_point = segment_start + intersection * segment_vector

                    r_segment = copy(segment)
                    r_segment.pos = segment_start, intersection_point
                    r_segment.vector = r_segment.pos[1] - r_segment.pos[0]
                    
                    l_segment = copy(segment)
                    l_segment.pos = intersection_point, segment_end
                    l_segment.vector = l_segment.pos[1] - l_segment.pos[0]

                    if numerator > 0:
                        l_segment, r_segment = r_segment, l_segment
                    
                    front_segment.append(r_segment)
                    back_segment.append(l_segment)
                    continue

            if numerator < 0 or (numerator_is_zero and denominator > 0):
                front_segment.append(segment)
            
            elif numerator > 0 or (numerator_is_zero and denominator < 0):
                back_segment.append(segment)

        self.add_segment(splitter_segment, node)
        return front_segment, back_segment    


    def add_segment(self, splitter_seg: Segment, node: BSPNode):
        self.segments.append(splitter_seg)
        node.segment_id = self.seg_id
            
        self.seg_id += 1
        
    def build(self, node:BSPNode, segments:list[Segment]):
        
        if not Segment:
            return None

        front_segment, back_segment = self.split_space(node, segments)

        if back_segment :
            node.back = BSPNode()
            self.build(node.back, back_segment)

        if front_segment:
            node.front = BSPNode()
            self.build(node.front, front_segment)


