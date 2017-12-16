# variables
line_distance_vect = PVector(-50, 0)
line_point1 = PVector(400, 390)
rotation_speed =  -0.1

def setup():
    size(800, 400)

def draw():
    global line_point1
    global rotation_speed
    global line_distance_vect
    global line_angle

    background(255)

    # this makes the line

    line(line_point1.x, line_point1.y, line_point1.x + line_distance_vect.x, line_point1.y + line_distance_vect.y)
    
    line_angle = degrees(line_distance_vect.heading())
    
    if line_angle < -180 or line_angle > 0:
        rotation_speed = - rotation_speed

    line_distance_vect.rotate(rotation_speed)

def mousePressed():
    global rotation_speed
    global line_angle
    rotation_speed = 0
    print(line_angle)
    
