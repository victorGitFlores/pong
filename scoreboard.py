from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0, 225)
        self.score_play_l = 0
        self.score_play_r = 0
        self.pencolor("white")
        self.hideturtle()  #hides the arrow

    def upd_score(self, p_lr):
        if p_lr == "l":
            self.score_play_l += 1
        if p_lr == "r":
            self.score_play_r += 1

    def dsp_score(self):
        self.penup()

        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.score_play_l}", font=FONT, align=ALIGNMENT)
        self.goto(100, 200)
        self.write(f"{self.score_play_r}", font=FONT, align=ALIGNMENT)