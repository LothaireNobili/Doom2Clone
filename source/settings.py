#configuration and options of the game
import pyray as ray
import glm
from glm import vec2, vec3, ivec2, normalize, cross, dot, atan2, sin, cos, length #common function we explicitely import to make the code easier to read

#resolution
WIN_RES = WIN_WIDTH, WIN_HEIGHT = 1600, 900
MAP_OFFSET = 50
MAP_WIDTH, MAP_HEIGHT = WIN_WIDTH - MAP_OFFSET, WIN_HEIGHT - MAP_OFFSET