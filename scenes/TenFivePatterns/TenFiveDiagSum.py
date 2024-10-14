from manim import *
from templates import TenFivePattern

class TenFiveDiagSum(TenFivePattern):
    def construct(self):
        super().construct()
        with self.voiceover(
            """Now on the other diagonal, we see that sums will form, and that they kind of form 'inward' as two overlapping sets of sums from different directions."""
        ):
            s = Tex("Down-Left Diagonals (below the top row) form ", "sums", " pointing inward", font_size=34)
            s[1].set_color_by_gradient(self.HIGHLIGHT, RED)
            self.writeSummary(s)

        with self.voiceover(
            """So from the top, we see 7 plus 4 is 11 (or 1 mod 10), and from the other end, we see 3 plus 1 is 4."""
        ):
            self.playDemo(0)

        with self.voiceover(
            """And this continues all the way down the grid, with one number always needing to be reduced mod 10.
            Remember, similar to the last diagonal, this actually talks about every 4th Fibonacci number, because it's one less than moving over by a column."""
        ):
            for i in range(1, 12):
                self.playDemo(i)
            self.cleanup()

    def playDemo(self, index):
        def getSelection(n):
            return self.getSelection(4, 4, 4, n)
                
        def makeDemo(mod=False):
            sel = [int(tex.get_tex_string()) for tex in getSelection(index)]
            demo = VGroup(
                self.makeEquation(sel[3], sel[2], mod).set_color_by_gradient(RED, ORANGE),
                self.makeEquation(sel[0], sel[1], mod, reverse=True).set_color_by_gradient(self.HIGHLIGHT, ORANGE))
            demo.scale(2).arrange(DOWN).next_to(self.grid, RIGHT, buff=0.5)

            def demoUpdater(demo):
                demo[1][0].align_to(demo[0][2], RIGHT)
                demo[1][1].move_to(
                    (demo[0][-2].get_center()[0], *demo[1][1].get_center()[1:])
                )
                demo[1][2:].align_to(demo[0][-1], LEFT)

            return demo.add_updater(demoUpdater)
        
        first = not self.demo

        introAnims = [getSelection(index).animate.set_color_by_gradient(self.HIGHLIGHT, RED)] # highlight the new set
        if first:
            self.demo = makeDemo().scale(0) # if this is our first animation, hide the demo but in the right position
        else:
            introAnims += [self.unhighlight(getSelection(index-1))] # otherwise, unhighlight the last selection
        introAnims += [self.demo.animate.become(makeDemo(not first))] # become the current selection
        self.play(*introAnims) # play all our intro animations
        sel = [int(tex.get_tex_string()) for tex in getSelection(index)]
        if first and (sel[3]+sel[2] >= 10 or sel[0]+sel[1] >= 10):
            self.wait(0.5)
            self.play(self.demo.animate.become(makeDemo(True)))
            self.wait()
        self.wait(0.5)
      