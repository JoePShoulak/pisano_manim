from manim import *
from templates import TenFivePattern

class TenFiveFrequency(TenFivePattern):
    def construct(self):
        super().construct()
        self.writeSummary(Tex("Numbers of the same parity have the same ", "frequency", font_size=34).set_color_by_tex("frequency", self.HIGHLIGHT))
        for i in range(2):
            self.playDemo(i)
        self.cleanup()

    def playDemo(self, index):
        def getSelection(n):
            return VGroup(*list(filter(lambda t : int(t.get_tex_string()) == n, self.grid)))
        
        def makeDemo():
            demo = VGroup(*[Tex(f"\# of {index+2*i}s: {len(getSelection(index+2*i))}", color=self.HIGHLIGHT) for i in range(5)])
            return demo.scale(1.25).arrange(DOWN).next_to(self.grid, RIGHT).to_edge(RIGHT, buff=3)

        if self.demo:
            self.play(FadeOut(self.demo))
            self.wait(0.5)

        self.demo = makeDemo()
        color = RED if index else ORANGE

        for i in range(6):
            if i > 0:
                self.play(
                    self.highlight(self.demo[i-1], color),
                    self.highlight(getSelection(index+2*(i-1)), color)
                )
            if i < 5:
                self.play(Write(self.demo[i]), self.highlight(getSelection(index+2*i)))
            self.wait(0.5)
        self.wait(0.5)
