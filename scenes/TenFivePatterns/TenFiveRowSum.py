from manim import *
from templates import TenFivePattern

class TenFiveRowSum(TenFivePattern):
    def construct(self):
        super().construct()

        with self.voiceover(
            """Now that we've proven most of the rows are the same, its easier to demonstrate that they all add across
            """
        ):
            self.writeSummary(Tex("Rows also have a pattern with ", "sums", font_size=55).set_color_by_tex("sums", self.HIGHLIGHT))

        with self.voiceover(
            """Remember, it totally makes sense that they add down, that's how this grid is defined.
            """
        ):
            self.playDemo(0)

        with self.voiceover(
            """But the fact that this works all the way around in another direction? If nothing else, 
            at this point you have to say there's more patterns than you expected to see. 
            """
        ):
            for i in range(12):
                self.playDemo(i)

        self.cleanup()

    def playDemo(self, index):
        def getSelection(n):
            return self.getSelection(1, 5, 3, n)
                
        def makeDemo(): 
            sel = [int(tex.get_tex_string()) for tex in getSelection(index)]
            return self.makeEquation(sel[0], sel[1], True).scale(2).next_to(self.grid, RIGHT).to_edge(RIGHT, buff=1.5)

        first = not self.demo
        
        introAnims = [getSelection(index).animate.set_color(self.HIGHLIGHT)] # highlight the new set
        if first:
            self.demo = makeDemo().scale(0) # if this is our first animation, hide the demo but in the right position
        else:
            introAnims += [self.unhighlight(getSelection(index-1)[0])] # otherwise, unhighlight the last selection
        introAnims += [self.demo.animate.become(makeDemo())] # become the current selection
        self.play(*introAnims) # play all our intro animations
        if first:
            self.wait()
        self.wait(0.5)
      