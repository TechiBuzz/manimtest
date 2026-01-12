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

        ball1 = SVGMobject(BALL_IMAGE).scale(0.2).next_to(car.get_top(), UP)
        self.add(ball1)
        self.play(Write(ball1), run_time=0.5)

        self.wait(4)
        vel = always_redraw(lambda: Arrow().next_to(car.get_right()))
        self.play(Write((vel)), Write(MathTex("v_b").next_to(vel)))

        self.wait()

        path1 = FunctionGraph(lambda x: -1, x_range=[-5.2, -3])
        path2 = FunctionGraph(lambda x: -(np.pow(x - 0.75, 2) - 5)/4 + 1.3 , x_range=[-3, 4.5])
        path3 = FunctionGraph(lambda x: -2, x_range=[-5.2, 4.5])

        # Adding both paths
        path1.append_points(path2.points)

        self.play(MoveAlongPath(ball1, path1), MoveAlongPath(car, path3), run_time=6, rate_func=linear)

        self.wait()