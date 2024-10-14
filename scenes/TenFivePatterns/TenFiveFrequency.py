from manim import *
from templates import TenFivePattern

class TenFiveFrequency(TenFivePattern):
    def construct(self):
        super().construct()
        with self.voiceover(
            """Now this time we won't be searching on lines, but we will find some!"""
        ):
            self.writeSummary(Tex("Numbers of the same parity have the same ", "frequency", font_size=34).set_color_by_tex("frequency", self.HIGHLIGHT))

        with self.voiceover(
            """If we look at the numbers of 0s... 2s... 4s... 6s... and 8s... we see they're all the same!"""
        ):
            self.playDemo(0)

        with self.voiceover(
            """And the same is true for 1s... 3s... 5s... 7s... and 9s... but just with twice as many of each!"""
        ):
            self.playDemo(1)

        with self.voiceover("And even when we're not looking for diagonals, they can still show up!"):
            self.wait_for_voiceover()

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
