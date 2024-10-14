from source.settings import *

#level prototyp, they will be created more smoothly in the future
P_00 = (0.0, 0.0)
P_01 = (0.0, 5.0)
P_10 = (7.0, 0.0)
P_11 = (7.0, 5.0)

SEGMENTS = [
    (P_00, P_01),
    (P_01, P_11),
    (P_11, P_10),
    (P_10, P_00)
]