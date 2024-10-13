from manim import *
from templates import TenFivePattern

class TenFiveDiagSum(TenFivePattern):
    def construct(self):
        super().construct()
        s = Tex("Down-Left Diagonals (below the top row) form ", "sums", " pointing inward", font_size=34)
        s[1].set_color_by_gradient(self.HIGHLIGHT, RED)
        self.writeSummary(s)
        for i in range(12):
            self.playDemo(i)
        self.cleanup()

    def playDemo(self, index):
        def getSelection(n):
            return self.getSelection(4, 4, 4, n)
                
        def makeDemo():
            sel = [int(tex.get_tex_string()) for tex in getSelection(index)]
            demo = VGroup(
                self.makeEquation(sel[3], sel[2]).set_color_by_gradient(RED, ORANGE),
                self.makeEquation(sel[0], sel[1], reverse=True).set_color_by_gradient(self.HIGHLIGHT, ORANGE))
            demo.scale(2).arrange(DOWN).next_to(self.grid, RIGHT, buff=0.5)

            def demoUpdater(demo):
                demo[1][0].align_to(demo[0][2], RIGHT)
                demo[1][1].move_to(
                    (demo[0][-2].get_center()[0], *demo[1][1].get_center()[1:])
                )
                demo[1][2:].align_to(demo[0][-1], LEFT)

            return demo.add_updater(demoUpdater)
        
        def reducedAnim(n1, n2, i, color=self.HIGHLIGHT):
            newEq = self.makeEquation(n1, n2, mod=True, reverse=i==1).set_color_by_gradient(color, ORANGE)
            newEq.scale(2).move_to(self.demo[i].get_center()).align_to(self.demo[i], LEFT)
            return self.demo[i].animate.become(newEq)
        
        first = not self.demo

        introAnims = [getSelection(index).animate.set_color_by_gradient(self.HIGHLIGHT, RED)] # highlight the new set
        if first:
            self.demo = makeDemo().scale(0) # if this is our first animation, hide the demo but in the right position
        else:
            introAnims += [self.unhighlight(getSelection(index-1))] # otherwise, unhighlight the last selection
        introAnims += [self.demo.animate.become(makeDemo())] # become the current selection
        self.play(*introAnims) # play all our intro animations
        sel = [int(tex.get_tex_string()) for tex in getSelection(index)]
        reduceAnims = []
        if sel[3]+sel[2] >= 10:
            reduceAnims.append(reducedAnim(sel[3], sel[2], 0, RED))
        if sel[0]+sel[1] >= 10:
            reduceAnims.append(reducedAnim(sel[0], sel[1], 1))
        if reduceAnims:
            self.wait(0.5)
            self.play(*reduceAnims)
        if first:
            self.wait()
        self.wait(0.5)
      