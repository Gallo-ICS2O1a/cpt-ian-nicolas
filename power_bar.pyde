speed = PVector(0, 10)
power_point = PVector(100, 100)
y1 = PVector(120, 125)
y2 = PVector(100, 150)
bad = color(230, 17, 17)
good = color(17, 230, 34)


def setup():
    size(500, 500)


def draw():
    global speed
    global power_point
    global bad
    global good
    background(255)
    noStroke()
    # Power Bar
    fill(bad)
    rect(100, 100, 50, 100)
    fill(good)
    rect(100, 200, 50, 100)
    fill(bad)
    rect(100, 300, 50, 100)

    stroke(10)
    fill(0)
    triangle(power_point.x, power_point.y, power_point.x + 20, power_point.y + 25, power_point.x, power_point.y + 50)
    power_point.add(speed)
    # y1.add(speed)
    # y2.add(speed)
    if power_point.y >= 350:
        speed = speed.mult(-1)
    elif power_point.y <= 100:
        speed = speed.mult(-1)


def mousePressed():
    global speed
    speed = speed.mult(0)
    power = PVector(0, 400 - power_point.y - 25, 0)
    print(power)
