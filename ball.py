from turtle import Turtle
from time import sleep

BALL_START_SPEED = 10
BALL_SPEEDER_FACTOR = 1
POST_PAD_BOUNCE_SLEEP = .11
POST_PAD_BOUNCE_SLEEP_FACTOR = .96
new_sleep_time = POST_PAD_BOUNCE_SLEEP

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.turtlesize(1,1)
        self.moveby = BALL_START_SPEED
        self.moving_ud = " "
        self.moving_rl = " "

    def move(self):
        if self.moving_ud == "u" and self.moving_rl == "r":
            x = self.xcor() + self.moveby
            y = self.ycor() + self.moveby
        if self.moving_ud == "u" and self.moving_rl == "l":
            x = self.xcor() - self.moveby
            y = self.ycor() + self.moveby
        if self.moving_ud == "d" and self.moving_rl == "r":
            x = self.xcor() + self.moveby
            y = self.ycor() - self.moveby
        if self.moving_ud == "d" and self.moving_rl == "l":
            x = self.xcor() - self.moveby
            y = self.ycor() - self.moveby

        self.setpos((x, y))
        #sleep(.11)
        sleep(new_sleep_time)

    def ck_collision_tb(self): # check for collisions on top and bot
        # returns t(collision top), b(collision bot), or blank (no collision)
        coll_top_bot = " "
        if self.ycor() > 285:
            self.moving_ud = "d"
        elif self.ycor() < -285:
            self.moving_ud = "u"

    def ck_collision_pad(self, pad): # check for collisions w paddle -flip r/l
        hit = False
        if self.xcor() > 332 or self.xcor() < -332:
            if self.ycor() > (pad.ycor() - 50) and self.ycor() < (pad.ycor() + 50):
                if self.moving_rl == "r":
                    self.moving_rl = "l"
                else:
                    self.moving_rl = "r"
                hit = True
                #speed things up
                self.new_sleep_time *= POST_PAD_BOUNCE_SLEEP_FACTOR
        return hit

    def ck_point(self):
        point = " "
        if self.xcor() > 380:
            point = "l"

        if self.xcor() < -380:
            point = "r"
        return point

    def speedup(self):
        #self.moveby *= 1.2
        pass

    def reset_speed(self):
        self.moveby = BALL_START_SPEED
        #note that teacher likes method below
        self.new_sleep_time = POST_PAD_BOUNCE_SLEEP