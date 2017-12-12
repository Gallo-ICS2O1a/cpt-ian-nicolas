player_size = 100
ball = PVector(400, 300)
ball_size = 50
speed = PVector(0, 0)
score = 0


def setup():
    size(800, 400)


def draw():
    global player_size
    global ball
    global ball_size
    global speed
    global score
    background(255)

    # Field
    noStroke()
    fill(18, 173, 42)
    rect(0, 200, 800, 200)

    # Net
    stroke(0)
    strokeWeight(5)
    fill(255)
    rect(300, 100, 200, 100)

    # Player
    noStroke()
    fill(255)
    player = PVector(mouseX, mouseY)
    ellipse(player.x, player.y, player_size, player_size)

    # Ball
    fill(0)
    ellipse(ball.x, ball.y, ball_size, ball_size)
    ball.add(speed)

    # Collision Detection
    coordinate_distance = PVector.sub(player, ball)
    # print(coordinate_distance)
    distance = coordinate_distance.mag()
    # print(distance)
    angle = coordinate_distance.heading()
    # print(angle)
    player_vector = PVector.fromAngle(angle)
    # print(player_vector)

    if distance <= player_size/2 + ball_size/2:
        speed.sub(player_vector)

    # Score Keeping
    if ball.x >= 300 and ball.x <= 500 and ball.y <= 200 and ball.y >= 100:
        score += 1

    text("Score: " + str(score), 100, 100)
