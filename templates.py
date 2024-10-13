from manim import *

def pisanoSequence(m):
    ps = [0, 1]
    while ps[-2:] != [1, 0]:
        ps.append((ps[-2] + ps[-1]) % m)
    return ps[:-1]

HIGHLIGHT = YELLOW_D

# TODO: Make a custom class for all scenes to inherit from; we have enough helpers to merit it

class TenFivePattern(Scene):
    def construct(self):
        self.HIGHLIGHT = HIGHLIGHT

        self.title = Text("Patterns", font_size=89).to_edge(UP)

        self.label = MathTex("P(", "10", ",", "5", ")")
        self.label.set_color_by_tex("10", RED).set_color_by_tex("5", ORANGE)
        self.label.scale(1.875).to_edge(UL)

        # Placeholder for cleanup
        self.summary = MathTex()
        self.demo = VGroup()

        self.grid = self.makeGrid()

        self.add(self.title)
        self.add(self.label)
        self.add(self.grid)
        self.wait()

    def makeGrid(self):
        grid = VGroup(*[Tex(n) for n in pisanoSequence(10)])
        return grid.arrange_in_grid(rows=5, cols=12, flow_order="dr").scale(1.25).center().to_edge(LEFT).shift(DOWN)

    def writeSummary(self, summary):
        self.summary = summary
        self.play(Write(self.summary.next_to(self.title, DOWN, buff=0.75))) 
        self.wait()

    def highlight(self, mob, color=HIGHLIGHT):
        return mob.animate.set_color(color)

    def unhighlight(self, mob):
        return self.highlight(mob, color=WHITE)
    
    def cleanup(self):
        self.play(FadeOut(self.summary), FadeOut(self.demo), self.unhighlight(self.grid))
        self.wait()
