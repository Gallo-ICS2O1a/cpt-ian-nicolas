speed=PVector(0, 1)
y=PVector(100, 100)
y1=PVector(150, 125)
y2=PVector(100, 150)
bad=color(230, 17, 17)
good=color(17, 230, 34)
def setup():
    size(500, 500)

def draw():
    global speed
    global y
    global bad
    global good    
    background(255)
    noStroke()
    fill(bad)
    rect(100, 100, 50, 100)
    fill(good)
    rect(100, 200, 50, 100)
    fill(bad)
    rect(100, 300, 50, 100)
    fill(0)
    triangle(y.x, y.y, y1.x, y1.y, y2.x, y2.y)
    y.add(speed)
    y1.add(speed)
    y2.add(speed)
    if y2.y>400:
        speed=speed.mult(-1)
    elif y.y<100:
        speed=speed.mult(-1)
def mouseClicked():
    global speed
    speed=speed.mult(0)
