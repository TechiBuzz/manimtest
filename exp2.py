from assets import CAR_IMAGE, GUN_IMAGE, GUN_FIRE_IMAGE, BULLET_IMAGE
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
        self.play(car.animate.to_edge(LEFT).shift(DOWN))

        # Create gun
        gun = SVGMobject(GUN_IMAGE).scale(0.4)
        gun.add_updater(lambda gun: gun.next_to(car.get_top(), UP))

        self.play(Write(gun))
        self.wait(2)

        # Create velocity vector
        vel = Arrow().next_to(car.get_right())
        vel_text = MathTex("v_b").next_to(vel).next_to(vel.get_end(), RIGHT)

        vel2 = Arrow().next_to(gun.get_right()).scale(0.8).shift(UP*0.25)
        vel_text2 = MathTex("v_b").next_to(vel2).next_to(vel2.get_end(), RIGHT).scale(0.8)

        self.play(Write(vel), Write(vel_text))
        self.play(Write(vel2), Write(vel_text2))
        self.wait(2)
        self.play(Unwrite(vel), Unwrite(vel_text), Unwrite(vel2), Unwrite(vel_text2), run_time=0.7)
        self.wait(2)

        self.play(car.animate.to_edge(RIGHT), rate_func=linear, run_time=4)
        self.wait(3)

        self.play(car.animate.to_edge(LEFT))
        self.wait(3)

        vel3 = Arrow().next_to(gun.get_right()).scale(0.8).shift(UP*0.25)
        vel_text3 = MathTex("2v_b").next_to(vel3).next_to(vel3.get_end(), RIGHT).scale(0.8)

        self.play(Write(vel3), Write(vel_text3))
        self.wait(3)
        self.play(Unwrite(vel3), Unwrite(vel_text3))
        self.wait(0.5)

        self.play(car.animate.to_edge(RIGHT), rate_func=linear, run_time=4)
        self.wait()