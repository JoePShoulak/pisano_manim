from manim import *
from templates import TenFivePattern

class TenFiveDiagPalindrome(TenFivePattern):
    def construct(self):
        super().construct()

        with self.voiceover(
            """The first pattern we'll look at is on the down-right diagonal."""
        ):
            self.writeSummary(Tex("Down-Right Diagonals (below the top row) form ", "palindromes", font_size=34).set_color_by_tex("palindromes", self.HIGHLIGHT))
        with self.voiceover(
            """It's important to try to figure out what this diagonal is actually representing, in terms of the original sequence.
            Because our grid height is 5, going 'down' our sequence by 5 is the same as going 'right' by one column.
            <bookmark mark='since'/>Since this diagonal talks about going right one and down one, it's actually describing every 6th Fibonacci number.
            Neat, huh? Well, on to the next one!"""
        ):
            self.playDemo(0)
            self.wait_until_bookmark("since")
            for i in range(1, 12):
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
    