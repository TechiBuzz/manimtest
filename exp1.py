from assets import BALL_IMAGE, CAR_IMAGE
from manim import *

import numpy as np

class Exp1(Scene):
    def construct(self):
        # Title
        title = Text("Experiment 1: Particles").to_edge(UP)
        title[0:12].set_color(BLUE_C)

        # Create car
        car = SVGMobject(CAR_IMAGE).scale(0.8)
        self.play(Write(title), Write(car))

        # Move car down
        self.wait(0.5)
        self.play(car.animate.to_edge(LEFT).shift(DOWN * 2))

        # self.add(Dot().next_to(car.get_top(), UP))

        # Projectile path
        path1 = FunctionGraph(lambda c: -0.85, x_range=[-5.2, -3.1])
        path2 = Line(LEFT * 3.1, RIGHT * 5.15, path_arc=-1.7).shift(DOWN * 0.85)
        path1.append_points(path2.get_all_points())

        # Create ball
        ball = SVGMobject(BALL_IMAGE).scale(0.2).move_to(path1.get_start())
        self.play(Write(ball))
        self.wait(2)

        # Create velocity vector
        vel = always_redraw(lambda: Arrow().next_to(car.get_right()))
        vel_text = always_redraw(lambda: MathTex("v").next_to(vel).next_to(vel.get_end(), RIGHT))

        self.play(Write(vel), Write(vel_text))
        self.wait(2)
        self.play(Unwrite(vel), Unwrite(vel_text))

        self.play(car.animate.to_edge(RIGHT), MoveAlongPath(ball, path1, rate_func=rush_from), run_time=4, rate_func=linear)
        # self.add(Dot().next_to(car.get_top(), UP))
        self.wait(3)