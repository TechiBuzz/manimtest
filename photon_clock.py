from manim import *

class PhotonClock(Scene):
    def construct(self):
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
        photon = Dot(color=YELLOW, stroke_width=0.1).next_to(mirror_bottom.get_center(), UP, buff=0)

        # Add mirrors
        self.play(Create(mirror_top), Create(mirror_bottom), Write(mirror_lines))
        # Add the photon
        self.play(DrawBorderThenFill(photon))

        # Tick clock
        for _ in range(3):
            self.play(MoveAlongPath(photon, Line(mirror_bottom.get_center(), mirror_top.get_center(), buff=DEFAULT_DOT_RADIUS), rate_func=linear), run_time=0.8)
            self.play(MoveAlongPath(photon, Line(mirror_top.get_center(), mirror_bottom.get_center(), buff=DEFAULT_DOT_RADIUS), rate_func=linear), run_time=0.8)

        self.wait()