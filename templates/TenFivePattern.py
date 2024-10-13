from manim import *
from .PisanoScene import *

class TenFivePattern(PisanoScene):
    def construct(self):
        super().construct()
        self.title = Text("Patterns", font_size=89).to_edge(UP)
        self.label = self.makeGridLabel(10, 5)
        self.summary = MathTex()
        self.demo = VGroup()
        self.grid = self.makeGrid()

        self.add(self.title)
        self.add(self.label)
        self.add(self.grid)
        self.wait()

    def makeGrid(self):
        return super().makeGrid(10, 5).scale(1.25).center().to_edge(LEFT).shift(DOWN)

    def makeEquation(self, a, b, mod=False, reverse=False):
        arrow = r"\Leftarrow" if reverse else r"\Rightarrow"
        [eq, sum] = ["=", a+b] if not mod else [arrow, (a+b)%10]
        formula = [a, "+", b, eq, sum]

        if reverse: formula = list(reversed(formula))
        
        return MathTex(*formula).set_color(self.HIGHLIGHT)

    def getSelection(self, offset, distance, r, n):
        return VGroup(*[self.grid[(offset+distance*i+5*n) % 60] for i in range(r)])

    def writeSummary(self, summary, wait_time=1):
        self.summary = summary
        self.play(Write(self.summary.next_to(self.title, DOWN, buff=0.75))) 
        
        if wait_time: self.wait(wait_time)

    def highlight(self, mob, color=False):
        return mob.animate.set_color(color if color else self.HIGHLIGHT)

    def unhighlight(self, mob):
        return self.highlight(mob, color=WHITE)
    
    def cleanup(self):
        self.play(FadeOut(self.summary), FadeOut(self.demo), self.unhighlight(self.grid))
        self.wait()
