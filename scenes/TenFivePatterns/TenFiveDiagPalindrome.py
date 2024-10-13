from manim import *
from templates import TenFivePattern

class TenFiveDiagPalindrome(TenFivePattern):
    def construct(self):
        super().construct()
        self.writeSummary(Tex("Down-Right Diagonals (below the top row) form ", "palindromes", font_size=34).set_color_by_tex("palindromes", self.HIGHLIGHT))
        for i in range(12):
            self.playDemo(i)
        self.cleanup()

    def playDemo(self, index):
        def makeDemo():
            demo = VGroup(*[Tex(eqn.get_tex_string(), color=self.HIGHLIGHT) for eqn in getSelection(index)])
            return demo.scale(2).arrange(RIGHT, buff=1.0).next_to(self.grid, RIGHT).to_edge(RIGHT, buff=1.5)

        def getSelection(n):
            return self.getSelection(1, 6, 4, n)
        
        first = not self.demo

        introAnims = [self.highlight(getSelection(index))] # highlight the new set
        if first:
            self.demo = makeDemo().scale(0) # if this is our first animation, hide the demo but in the right position
        else:
            introAnims += [self.unhighlight(getSelection(index-1))] # otherwise, unhighlight the last selection
        introAnims += [self.demo.animate.become(makeDemo())] # become the current selection
        self.play(*introAnims) # play all our intro animations
        if first: # only demo the first reversal
            self.palindromeAnim({"mobj": self.demo, "sym": True})
        self.wait(0.5)
    