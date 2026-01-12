from assets import SPACESHIP_IMAGE
from manim import *

class LengthContraction(Scene):
    def construct(self):
        title = Text("Length Contraction").to_edge(UP).scale(0.7)
        title[:6].set_color(PURPLE_C)
        self.play(Write(title))

        ship1 = SVGMobject(SPACESHIP_IMAGE).scale(0.4)
        plat1 = NumberLine(x_range=[1, 15],include_numbers=True, length=13).shift(UP * 0.6)

        ship2 = SVGMobject(SPACESHIP_IMAGE).scale(0.4)
        plat2 = NumberLine(x_range=[1, 15],include_numbers=True, length=13).shift(DOWN * 2.8)

        d1 = Dot(color=GREEN_C).next_to(plat1.numbers[2], UP).shift(DOWN * DEFAULT_DOT_RADIUS)

        d2 = Dot(color=GREEN_C).next_to(plat1.numbers[10], UP).shift(DOWN * DEFAULT_DOT_RADIUS)

        d3 = Dot(color=GREEN_C)
        d3.add_updater(lambda dot: dot.next_to(plat2.numbers[2], UP).shift(DOWN * DEFAULT_DOT_RADIUS))

        d4 = Dot(color=GREEN_C)
        d4.add_updater(lambda dot: dot.next_to(plat2.numbers[6], UP).shift(DOWN * DEFAULT_DOT_RADIUS))

        # Platform POV
        self.wait(3)
        self.play(Write(ship1))
        self.wait()

        self.play(ship1.animate.to_edge(LEFT).shift(UP * 1.8).shift(RIGHT), Write(plat1))
        
        label1 = Text("Platform's Frame").scale(0.4).next_to(ship1.get_top(), UP)
        self.play(Write(label1))

        gamma = MathTex("\\gamma = 2").next_to(label1).shift(RIGHT * 9).scale(0.7)
        gamma[0][0].set_color(GREEN_D)

        self.wait(2)
        self.play(Write(gamma))

        self.wait(4)
        # Move ship
        self.play(plat1.numbers[2].animate.set_color(YELLOW), Create(d1), run_time=0.3)
        self.play(ship1.animate.shift(RIGHT * 7.35), run_time=2.134, rate_func=linear)
        self.play(plat1.numbers[10].animate.set_color(YELLOW), Create(d2), run_time=0.3)

        self.wait(8)

        # Ship POV
        self.play(ship2.animate.to_edge(LEFT).shift(DOWN * 1.5).shift(RIGHT), Write(plat2))
        
        label2 = Text("Ship's Frame").scale(0.4).next_to(ship2.get_top(), UP)
        self.play(Write(label2))
        
        self.wait(4)

        # Move platform
        self.play(plat2.numbers[2].animate.set_color(YELLOW), Create(d3), run_time=0.3)
        self.play(plat2.animate.shift(LEFT * 3.7), run_time=1.6, rate_func=linear)
        self.play(plat2.numbers[6].animate.set_color(YELLOW),  Create(d4), run_time=0.3)
        self.wait(2)

        # Reset bottom platform
        self.play(plat2.animate.shift(RIGHT * 3.7))
        self.wait(4)

        # Remove dot updaters
        d3.clear_updaters()
        d4.clear_updaters()

        # Shrink platform
        self.play(plat2.animate.stretch(0.5, dim=0, about_point=plat2.numbers[2].get_center()))
        self.wait(4)

        # Shrink ship
        self.play(ship1.animate.stretch(0.5, dim=0))
        self.wait(4)

        # Remove everything

        self.play(
            Uncreate(d1),
            Uncreate(d2),
            Uncreate(d3),
            Uncreate(d4),
            Unwrite(label1),
            Unwrite(label2),
            Unwrite(ship1),
            Unwrite(ship2),
            Unwrite(plat1),
            Unwrite(plat2),
            Unwrite(gamma),
            run_time=1.5
        )

        self.wait(2)

        # Equation
        eqn = MathTex("L'" + "=" + "\\frac{L}{\\gamma}")
        eqn[0][5].set_color(GREEN_D)

        self.play(Write(eqn))
        self.wait(1.5)

        self.play(eqn.animate.scale(1.5))
        self.play(eqn.animate.shift(UP * 1.3))

        box_to_eq8 = SurroundingRectangle(eqn, buff=0.4, color=YELLOW_D)
        self.play(Write(box_to_eq8))
        self.wait(1.5)

        gamma = MathTex("\\gamma = \\frac{1}{\\sqrt{1 - \\frac{v^2}{c^2}}}").move_to(eqn).shift(DOWN * 3)
        gamma[0][0].set_color(GREEN_D)

        box_to_gamma = SurroundingRectangle(gamma, buff=0.4, color=GREEN)
        self.play(Write(box_to_gamma), Write(gamma), run_time=2)
        self.wait(4)

