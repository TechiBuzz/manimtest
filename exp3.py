from assets import CAR_IMAGE, TORCH_IMAGE
from manim import *

import numpy as np

class Exp3(Scene):
    def construct(self):
        # Title
        title = Text("Experiment-3: Light").to_edge(UP).shift(DOWN*0.25)
        title[0:12].set_color(GREEN_B)

        # Create car
        car = SVGMobject(CAR_IMAGE).scale(0.8)
        self.play(Write(title), Write(car))

        # Move car down
        self.wait(0.5)
        self.play(car.animate.to_edge(LEFT).shift(DOWN))

        # Create gun
        torch = SVGMobject(TORCH_IMAGE).scale(0.3)
        torch.add_updater(lambda gun: gun.next_to(car.get_top(), UP))

        self.play(Write(torch))
        self.wait(2)

        # Create velocity vectors
        vel = Arrow().next_to(car.get_right())
        vel_text = MathTex("c").next_to(vel).next_to(vel.get_end(), RIGHT)

        vel2 = Arrow().next_to(torch.get_right()).scale(0.8)
        vel_text2 = MathTex("c").next_to(vel2).next_to(vel2.get_end(), RIGHT).scale(0.8)

        self.play(Write(vel), Write(vel_text))
        self.play(Write(vel2), Write(vel_text2))
        self.wait(2)

        self.play(Unwrite(vel), Unwrite(vel_text), Unwrite(vel2), Unwrite(vel_text2), run_time=0.7)
        self.wait(2)

        # Move car right
        self.play(car.animate.to_edge(RIGHT), rate_func=linear, run_time=4)
        self.wait(3)