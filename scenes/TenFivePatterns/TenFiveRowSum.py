from manim import *
from templates import TenFivePattern

class TenFiveRowSum(TenFivePattern):
    def construct(self):
        super().construct()
        self.writeSummary(Tex("Rows also have a pattern with ", "sums", font_size=55).set_color_by_tex("sums", self.HIGHLIGHT))
        for i in range(12):
            self.playDemo(i)
        self.cleanup()

    def playDemo(self, index):
        def getSelection(n):
            return self.getSelection(1, 5, 3, n)
                
        def makeDemo(mod=False): 
            sel = [int(tex.get_tex_string()) for tex in getSelection(index)]
            return self.makeEquation(sel[0], sel[1], mod).scale(2).next_to(self.grid, RIGHT).to_edge(RIGHT, buff=1.5)

        first = not self.demo
        
        introAnims = [getSelection(index).animate.set_color(self.HIGHLIGHT)] # highlight the new set
        if first:
            self.demo = makeDemo().scale(0) # if this is our first animation, hide the demo but in the right position
        else:
            introAnims += [self.unhighlight(getSelection(index-1)[0])] # otherwise, unhighlight the last selection
        introAnims += [self.demo.animate.become(makeDemo())] # become the current selection
        self.play(*introAnims) # play all our intro animations
        sel = [int(tex.get_tex_string()) for tex in getSelection(index)]
        if sel[0] + sel[1] >= 10:
            self.play(self.demo.animate.become(makeDemo(True).align_to(self.demo, LEFT)))
        if first:
            self.wait()
        self.wait(0.5)
      