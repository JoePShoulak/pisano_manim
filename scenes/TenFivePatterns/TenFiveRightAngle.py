from manim import *
from templates import TenFivePattern

class TenFiveRightAngle(TenFivePattern):
    def construct(self):
        super().construct()
        with self.voiceover("This next pattern is a bit special because it's not a straight line, but a corner!"):
            self.writeSummary(Tex("Right Angles at the bottom (\"pointing\" down-right) ", "repeat", font_size=34).set_color_by_tex("repeat", self.HIGHLIGHT))
        
        with self.voiceover(
            """We can see here that we get this cyclic pattern, skipping over the corner that defines it.
            """
        ):
            self.playDemo(0)

        with self.voiceover(
            """One thing I haven't clarified explicitly is that because the Fibonacci sequence repeats with a given modulus,
            and the grid is some grid where the height divides the period, the grid 'does' repeat infinitely in both directions.
            Because of this, finding a pattern the way we're doing 'actually' proves it. No algebra, no 'only-kind-of', we proved it.
            """
        ):
            for i in range(1, 12):
                self.playDemo(i)

        self.cleanup()

    def playDemo(self, index):
        def makeDemo():
            demo = VGroup(*getSelection(index)).copy().scale(2/1.5)
            for d in demo[:-1]:
                d.color = self.HIGHLIGHT
            demo[3].next_to(demo[2], RIGHT)
            demo[4].next_to(demo[3], RIGHT)
            demo[0].next_to(demo[4], UP)
            demo[1].next_to(demo[0], UP)
            return demo.next_to(self.grid, RIGHT).to_edge(RIGHT, buff=3)

        # This is kinda horrible, but it lets me arrange in grid how I want
        def getSelection(n):
            return VGroup(
                *list(reversed(self.getSelection(12, 1, 2, n))),
                *self.getSelection(4, 5, 2, n),
                self.grid[(14+5*n) % 60]
            )
        
        first = not self.demo
        
        introAnims = [self.highlight(getSelection(index)[:-1])] # highlight the new set
        if first:
            self.demo = makeDemo().scale(0) # if this is our first animation, hide the demo but in the right position
        else:
            introAnims += [self.unhighlight(getSelection(index-1)[i]) for i in [0, 1, 2]] # otherwise, unhighlight the last selection
        introAnims += [self.demo.animate.become(makeDemo())] # become the current selection
        self.play(*introAnims) # play all our intro animations
        if first:
            self.wait()
            miniGrid = VGroup(*self.demo[:-1])
            self.play(
                miniGrid.animate.arrange_in_grid(rows=2),
                FadeOut(self.demo[-1], scale=0)
            )
            self.demo[-1].scale(0)
        self.wait(0.5)
     