from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("P O N G")
screen.tracer(0)

scoreboard = Scoreboard()


def flip_server():
    global server
    if server == "l":
        server = "r"
    else:
        server = "l"
# ====================================================


def game_start(p_ball, p_pad_l, p_pad_r):
    global server
    sleep(1)
    p_ball.setpos((0, 0))
    p_pad_l.setpos((-350, 0))
    p_pad_r.setpos((350, 0))
    p_pad_r.color("red")
    p_pad_l.color("white")

    p_ball.moving_ud = "u"
    if server == "r":
        p_ball.moving_rl = "l"
        p_ball.color("red")
    else:
        p_ball.moving_rl = "r"
        p_ball.color("white")

    ball.reset_speed()

# ====================================================



paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))

ball = Ball()
screen.listen()
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")


server = "l"
game_start(ball, paddle_left, paddle_right)
game_on = True


while game_on:
    scoreboard.dsp_score()
    screen.update()
    ball.move()
    #
    ball.ck_collision_tb()
    if ball.ck_collision_pad(paddle_left):
        ball.move()
        ball.speedup()

    if ball.ck_collision_pad(paddle_right):
        ball.move()
        ball.speedup()


    point = ball.ck_point()
    if point == "r":
        scoreboard.upd_score("r")
    if point == "l":
        scoreboard.upd_score("l")
    if point != " ":
        flip_server()
        game_start(ball, paddle_left, paddle_right)






#stay on screen till click
screen.exitonclick()



