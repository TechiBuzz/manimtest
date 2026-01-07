from manim import *
import numpy as np

class PhotonClock(Scene):
    def tick_clock(self, photon, mirror_top, mirror_bottom, ticks):
        for _ in range(ticks):
            self.play(MoveAlongPath(photon, Line(mirror_bottom.get_center(), mirror_top.get_center(), buff=DEFAULT_DOT_RADIUS), rate_func=linear), run_time=0.8)
            self.play(MoveAlongPath(photon, Line(mirror_top.get_center(), mirror_bottom.get_center(), buff=DEFAULT_DOT_RADIUS), rate_func=linear), run_time=0.8)


    def construct(self):
        # Text
        text = Text("Photon Clock").to_edge(UP).scale(0.5)

        # Mirror
        mirror_top = Line(LEFT, RIGHT).shift(UP)
        mirror_bottom = Line(LEFT, RIGHT).shift(DOWN)

        mirror_lines = VGroup()
        for i in range(11):
            mirror__bottom_line = Line(mirror_bottom.get_start(), mirror_bottom.get_start()+0.2*DOWN)
            mirror__bottom_line.rotate(-30*DEGREES, about_point=mirror_bottom.get_start())
            mirror__bottom_line.shift(0.2*i*RIGHT)

            mirror_top_line = Line(mirror_top.get_start(), mirror_top.get_start()+0.2*DOWN)
            mirror_top_line.rotate(-150*DEGREES, about_point=mirror_top.get_start())
            mirror_top_line.shift(0.2*i*RIGHT)

            mirror_lines.add(mirror_top_line)
            mirror_lines.add(mirror__bottom_line)

        # Photon
        photon = Dot(color=YELLOW, stroke_width=0.1).next_to(mirror_bottom.get_center(), UP, buff=0.02)

        # Clock Label
        clock_label = Text("Observer").next_to(mirror_bottom, DOWN).scale(0.4)

        # Clocks
        photon_clock_obs = VGroup(photon, mirror_top, mirror_bottom, mirror_lines, clock_label)
        photon_clock_ship = photon_clock_obs.copy()

        # Create the clock
        self.play(Write(text), run_time=2)
        self.play(Create(mirror_top), Create(mirror_bottom), Write(mirror_lines))
        self.play(DrawBorderThenFill(photon), run_time=0.7)
        self.wait()

        # Tick clock
        self.tick_clock(photon, mirror_top, mirror_bottom, 1)
        self.wait()

        # Keep aside the main clock
        self.play(Unwrite(text), Write(clock_label), run_time=1.5)
        self.play(photon_clock_obs.animate.to_edge(DL))
        self.wait()

        # Second clock
        self.play(Write(photon_clock_ship), run_time=2.5)
        self.play(photon_clock_ship.animate.to_edge(UL))
        self.wait()

        path = FunctionGraph(function=lambda x: (2 / np.pi) * np.arcsin(np.sin(np.pi * x / 2)), x_range=[- 3 / 2 * np.pi, 3 / 2 * np.pi])
        self.play(MoveAlongPath(photon, path, rate_func=linear), run_time=10)
        self.wait()