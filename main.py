from manim import *

class Test(Scene):
    def construct(self):
        mirror_top = Line([-1, 0, 0],[1, 0, 0]).shift(UP)
        mirror_btm = Line([-1, 0, 0],[1, 0, 0]).shift(DOWN)

        photon = Dot(color=YELLOW, fill_opacity=0.75, radius=0.1).shift(DOWN + 0.1)

        self.play(Create(mirror_top), Create(mirror_btm), DrawBorderThenFill(photon), run_time=2)
        self.wait(0.4)

        # for _ in range(3):
        #     self.play(MoveAlongPath(photon, Line(mirror_btm.get_top(), mirror_top.get_bottom(), buff=0.1), rate_func=linear), run_time=0.7)
        #     self.play(MoveAlongPath(photon, Line(mirror_top.get_bottom(), mirror_btm.get_top(), buff=0.1), rate_func=linear), run_time=0.7, rate_fun=linear)

        self.play(Create(Angle(mirror_btm, Line([-1, 1, 0],[1, 3, 0]), color=RED)))

        self.wait()