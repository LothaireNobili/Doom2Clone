from source.settings import *

#level prototyp, they will be created more smoothly in the future
P_00 = (1.0, 1.0)
P_01 = (1.0, 6.0)
P_11 = (8.0, 6.0)
P_10 = (8.0, 1.0)


SEGMENTS = [
    (P_00, P_01),
    (P_01, P_11),
    (P_11, P_10),
    (P_10, P_00)
]