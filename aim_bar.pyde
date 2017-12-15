line_distance_vect = PVector(-50, 0)
line_point1 = PVector(400, 390)
rotation_speed =  -0.1
rotation = 0

def setup():
    size(800, 400)

def draw():
    global line_point1
    global line_point2
    global rotation
    global rotation_speed
    global line_distance_vect
    
    background(255)

    # this makes the line
    line(line_point1.x, line_point1.y, line_point1.x + line_distance_vect.x, line_point1.y + line_distance_vect.y)

#     triangle(width + line_distance_vect.x, height + line_distance_vect.y, width + line_distance_vect.x + 25, height + line_distance_vect.y + 25, width + line_distance_vect.x + 25, height + line_distance_vect.y - 25)
    line_angle = degrees(line_distance_vect.heading())
    print(line_angle)

    if line_angle < -180 or line_angle > 0:
        rotation_speed = - rotation_speed

    line_distance_vect.rotate(rotation_speed)

    

    