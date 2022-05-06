from dataclasses import dataclass

@dataclass
class Const:
    #Everything in meters
    
    CANVAS_HEIGHT = 10
    CANVAS_WIDTH = 10
    ORIGIN_X = 0
    ORIGIN_Y = 0
    SKEW_WIDTH = 1
    
    RESOLUTION = 0.1    
    
    ROBOT_DIA = 0.25
    WALL_CLEARANCE = 0.25
    
    CLEARANCE = ROBOT_DIA + WALL_CLEARANCE
    