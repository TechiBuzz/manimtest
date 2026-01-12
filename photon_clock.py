from manim import *
import numpy as np

class PhotonClock(Scene):
    def tick_clock(self, clock, ticks):
        photon = clock[0]
        mirror_top = clock[1]
        mirror_bottom = clock[2]

        anim = [
            # Going up
            MoveAlongPath(
                photon, 
                Line(mirror_bottom.get_center(), mirror_top.get_center(), buff=DEFAULT_DOT_RADIUS), 
                rate_func=linear, 
                run_time=0.8
            ),
            # Coming down
            MoveAlongPath(
                photon, 
                Line(mirror_top.get_center(), mirror_bottom.get_center(), buff=DEFAULT_DOT_RADIUS), 
                rate_func=linear, 
                run_time=0.8
            )
        ]

        return anim * ticks

    def construct(self):
        # Text
        title = Text("Photon Clock").to_edge(UP).scale(0.7)

        # Mirror
        mirror_top = Line(LEFT, RIGHT).shift(UP)
        mirror_bottom = Line(LEFT, RIGHT).shift(DOWN)

        mirror_lines = VGroup()
        for i in range(11):
            mirror__bottom_line = Line(mirror_bottom.get_start(), mirror_bottom.get_start() + 0.2 * DOWN)
            mirror__bottom_line.rotate(-30 * DEGREES, about_point=mirror_bottom.get_start())
            mirror__bottom_line.shift(0.2 * i *RIGHT)

            mirror_top_line = Line(mirror_top.get_start(), mirror_top.get_start() + 0.2 * DOWN)
            mirror_top_line.rotate(-150 * DEGREES, about_point=mirror_top.get_start())
            mirror_top_line.shift(0.2 * i * RIGHT)

            mirror_lines.add(mirror_top_line)
            mirror_lines.add(mirror__bottom_line)

        # Photon
        photon = Dot(color=YELLOW, stroke_width=0.1).next_to(mirror_bottom.get_center(), UP, buff=0.02)

        # Clock Label
        clock_label = Text("Observer's Clock").next_to(mirror_bottom, DOWN).scale(0.4)

        # Clocks
        photon_clock_obs = VGroup(photon, mirror_top, mirror_bottom, mirror_lines, clock_label)

        photon_clock_ship = photon_clock_obs.copy()
        photon_clock_ship[4] = Text("Ship's Clock").next_to(photon_clock_ship[2], DOWN).scale(0.4)

        # Create the clock
        self.play(Write(title), run_time=2)
        self.play(Create(mirror_top), Create(mirror_bottom), Write(mirror_lines))
        self.play(DrawBorderThenFill(photon), run_time=0.7)
        self.wait()

        # Tick clock
        self.play(Succession([anim for anim in self.tick_clock(photon_clock_obs, 5)]))
        # self.tick_clock(photon, mirror_top, mirror_bottom, 5)
        self.wait()

        # Keep aside the main clock
        self.play(Unwrite(title), Write(clock_label), run_time=1.5)
        self.play(photon_clock_obs.animate.to_edge(DL))
        self.wait()

        # Second clock
        self.play(Create(photon_clock_ship[1]), Create(photon_clock_ship[2]), Write(photon_clock_ship[3]))
        self.play(DrawBorderThenFill(photon_clock_ship[0]), run_time=0.7)
        self.play(Write(photon_clock_ship[4]), run_time=1.5)
        
        # Keep aside second clock
        self.wait()
        self.play(photon_clock_ship.animate.to_edge(UL))
        self.wait(2)

        # Diagonal path for photon
        path = FunctionGraph(
            function=lambda x: ((1.9 / np.pi) * (np.arcsin(np.sin(np.pi * (x - 1) / 1.85)))) + 1,
            x_range=[0 + DEFAULT_DOT_RADIUS, 11.2], color=BLUE
        ).next_to(photon_clock_ship[2].get_center(), RIGHT, buff=0).shift(UP)
        path.z_index = -1

        # Trace
        trace = TracedPath(photon_clock_ship[0].get_center, color=BLUE)
        self.add(trace)

        # Move second clock horizontally and simultaneously tick the observer clock
        self.play(
            # move top clock right
            photon_clock_ship.animate(run_time=8*0.8).to_edge(RIGHT), 
            # move photon diagonally
            MoveAlongPath(photon_clock_ship[0], path, run_time=8*0.8), 
            # tick bottom clock
            Succession(self.tick_clock(photon_clock_obs, 4)), 
            rate_func=linear
        )
        self.wait(2)

        self.play(Write(path), run_time=4)

        # Erase everything except 1 clock
        self.play(Unwrite(path), Unwrite(trace), Unwrite(photon_clock_ship), Unwrite(clock_label))
        self.wait(4)

        # Time Dilation
        title = Text("Time Dialtion").to_edge(UP).scale(0.7)
        
        self.play(Write(title), photon_clock_obs.animate.shift(UP * 2).shift(RIGHT).scale(1.2))
        self.wait(3)

        arrow1 = Arrow(start=photon_clock_obs[2].get_center(), end=Point(photon_clock_obs[1].get_bottom()).shift(DOWN * DEFAULT_DOT_RADIUS), color=BLUE_B, stroke_width=2.5, tip_length=0.15, buff=0, z_index=-1)
        brace1 = BraceText(arrow1, text="ct", brace_direction=LEFT, font_size=32)

        self.play(Write(arrow1), Write(brace1))
        self.wait(2)

        duplicate = photon_clock_obs.copy()
        duplicate[0].move_to(duplicate[1].get_bottom(), UP)
        self.play(duplicate.animate.shift(RIGHT * 3))

        arrow2 = Arrow(start=arrow1.get_end(), end=duplicate[0].get_center(), color=ORANGE, stroke_width=2.5, tip_length=0.15, buff=0, z_index=1)
        brace2 = BraceText(arrow2, text="vt'", brace_direction=UP, font_size=32)

        arrow3 = Arrow(start=photon_clock_obs[0].get_center(), end=arrow2.get_end(), color=GREEN, stroke_width=2.5, tip_length=0.15, buff=0.05, z_index=-2)
        brace3 = BraceBetweenPoints(point_1=arrow3.get_start(), point_2=arrow3.get_end())
        brace3_text = Text(text="ct'", font_size=32).next_to(brace3, DOWN).shift(UP).shift(RIGHT*0.5)
        
        self.play(Write(arrow3), Write(brace3), Write(brace3_text))
        self.wait(3)

        self.play(Write(arrow2), Write(brace2))
        self.wait(5)

        # Equations
        eqnref = Dot().to_corner(UR).shift(LEFT * 3).shift(DOWN)
        eq1 = MathTex("(ct')^2" + "=" + "(ct)^2" + "+" + "(vt')^2").next_to(eqnref, DOWN)
        eq2 = MathTex("(ct')^2" + "-" + "(vt')^2" + "=" + "(ct)^2").next_to(eqnref, DOWN * 4)
        eq3 = MathTex("c^2t'^2" + "-" + "v^2t'^2" + "=" + "c^2t^2").next_to(eqnref, DOWN * 7)
        eq4 = MathTex("t'^2(c^2 - v^2)" + "=" + "c^2t^2").move_to(eq3)
        eq5 = MathTex("t'^2(1 - \\frac{v^2}{c^2})" + "=" + "t^2").move_to(eq3)
        eq6 = MathTex("t'^2" + "=" + "\\frac{t^2}{(1 - \\frac{v^2}{c^2})}").move_to(eq3)
        eq7 = MathTex("t'" + "=" + "\\frac{t}{\\sqrt{1 - \\frac{v^2}{c^2}}}").move_to(eq3)

        eq8 = MathTex("t'" + "=" + "\\gamma t").next_to(eqnref, DOWN * 7)
        eq8[0][3].set_color(GREEN_D)

        # Lorentz Factor things
        gamma = MathTex("\\gamma = \\frac{1}{\\sqrt{1 - \\frac{v^2}{c^2}}}").move_to(eq8).shift(DOWN).scale(1.4)
        gamma[0][0].set_color(GREEN_D)

        box_to_gamma = SurroundingRectangle(gamma, buff=0.4, color=GREEN)

        gamma_text = Text("Lorentz Factor", font_size=40).move_to(gamma).shift(DOWN * 1.9)
        gamma_text[0:7].set_color(GREEN_D)

        # Transform one equation to another
        self.play(Write(eq1))
        self.wait(2.5)
        self.play(Transform(eq1, eq2, replace_mobject_with_target_in_scene=True))
        self.wait(2.5)
        self.play(Transform(eq2, eq3, replace_mobject_with_target_in_scene=True))
        self.wait(2.5)
        self.play(Transform(eq3, eq4, replace_mobject_with_target_in_scene=True))
        self.wait(2.5)
        self.play(Transform(eq4, eq5, replace_mobject_with_target_in_scene=True))
        self.wait(2.5)
        self.play(Transform(eq5, eq6, replace_mobject_with_target_in_scene=True))
        self.wait(2.5)
        self.play(Transform(eq6, eq7, replace_mobject_with_target_in_scene=True))
        self.wait(2.5)
        self.play(Transform(eq7, eq8, replace_mobject_with_target_in_scene=True))
        self.wait(2)

        self.play(eq8.animate.scale(1.5))
        self.play(eq8.animate.shift(UP * 1.5))

        box_to_eq8 = SurroundingRectangle(eq8, buff=0.4, color=BLUE_D)
        self.play(Write(box_to_eq8))
        self.wait()

        self.play(Write(box_to_gamma), Write(gamma), Write(gamma_text), run_time=2)
        self.wait(10)

        # Remove for table
        self.play(
            Unwrite(photon_clock_obs), 
            Unwrite(duplicate), 
            Unwrite(arrow1), 
            Unwrite(brace1), 
            Unwrite(arrow2), 
            Unwrite(brace2), 
            Unwrite(arrow3), 
            Unwrite(brace3), 
            Unwrite(brace3_text),
            Unwrite(eq8),
            Unwrite(box_to_eq8),
            Unwrite(gamma),
            Unwrite(box_to_gamma),
            Unwrite(gamma_text)
        )
        self.wait(1.5)

        table = MathTable(table=[
            ["v", "\\gamma"], 
            ["0.5c", "1.2"],
            ["0.87c", "2"],
            ["0.999c", "22"],
            ["0.9999c", "70"]
            ],include_outer_lines=True)
        table[0][0][:].set_color(YELLOW).scale(1.2)
        table[0][1][0].set_color(GREEN).scale(1.2)

        self.play(Write(table.scale(0.8)))
        self.play(table.animate.scale(1.2))
        self.wait(3)