from assets import BALL_IMAGE, CAR_IMAGE
from manim import *

import numpy as np

class Exp1(Scene):
    def construct(self):
        title = Text("Experiment 1: Vertical Projectile").to_edge(UP)
        title[0:12].set_color(DARK_BLUE)

        car = SVGMobject(CAR_IMAGE).scale(0.8)
        self.play(Write(title), Write(car))

        self.wait(0.5)
        self.play(car.animate.to_edge(LEFT).shift(DOWN * 2))

        vel = Arrow().next_to(car.get_right())
        self.play(Write((vel)), Write(MathTex("v_b").next_to(vel)))

        ball = SVGMobject(BALL_IMAGE).scale(0.2).next_to(car.get_top(), UP)
        # self.add(Dot().next_to(car.get_top(), UP))
        self.play(Write(ball), run_time=0.5)

        self.wait(4)
        path = FunctionGraph(lambda x: -np.pow(x, 2)/12 + 1.38, x_range=[-5.2, 5.2])
        self.play(car.animate.to_edge(RIGHT), MoveAlongPath(ball, path), run_time=4, rate_func=linear)
        # self.add(Dot().next_to(car.get_top(), UP))

        
        # self.add(path)

        self.wait()