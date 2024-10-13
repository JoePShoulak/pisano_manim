from manim import *
from templates import TenFivePattern

class TenFiveRightAngle(TenFivePattern):
    def construct(self):
        super().construct()
        self.writeSummary(Tex("Right Angles at the bottom (\"pointing\" down-right) ", "repeat", font_size=34).set_color_by_tex("repeat", self.HIGHLIGHT))
        for i in range(12):
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
     