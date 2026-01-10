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
        photon_clock_ship[4] = Text("Ship").next_to(photon_clock_ship[2], DOWN).scale(0.4)

        # Create the clock
        self.play(Write(text), run_time=2)
        self.play(Create(mirror_top), Create(mirror_bottom), Write(mirror_lines))
        self.play(DrawBorderThenFill(photon), run_time=0.7)
        self.wait()

        # Tick clock
        self.play(Succession([anim for anim in self.tick_clock(photon_clock_obs, 5)]))
        # self.tick_clock(photon, mirror_top, mirror_bottom, 5)
        self.wait()

        # Keep aside the main clock
        self.play(Unwrite(text), Write(clock_label), run_time=1.5)
        self.play(photon_clock_obs.animate.to_edge(DL))
        self.wait()

        # Second clock
        self.play(Create(photon_clock_ship[1]), Create(photon_clock_ship[2]), Write(photon_clock_ship[3]))
        self.play(DrawBorderThenFill(photon_clock_ship[0]), run_time=0.7)
        self.play(Write(photon_clock_ship[4]), run_time=1.5)
        
        # Keep aside second clock
        self.wait()
        self.play(photon_clock_ship.animate.to_edge(UL))
        self.wait()

        # Move second clock horizontally and simultaneously tick the observer clock
        self.play(
            photon_clock_ship.animate(run_time=8*0.8).to_edge(RIGHT),
            Succession(self.tick_clock(photon_clock_ship, 5)),
            Succession(self.tick_clock(photon_clock_obs, 5)),
            rate_func=linear
        )

        self.wait()