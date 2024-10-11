from manim import *

def pisanoSequence(m):
    ps = [0, 1]
    while ps[-2:] != [1, 0]:
        ps.append((ps[-2] + ps[-1]) % m)
    return ps[:-1]

class TenFivePattern(Scene):
    def construct(self):
        self.title = Text("Patterns", font_size=89).to_edge(UP)

        self.label = MathTex("P(", "10", ",", "5", ")")
        self.label.set_color_by_tex("10", RED).set_color_by_tex("5", ORANGE)
        self.label.scale(1.875).to_edge(UL)

        self.summary = MathTex() # Placeholder for cleanup

        self.grid = VGroup(*[Tex(n) for n in pisanoSequence(10)])
        self.grid.arrange_in_grid(rows=5, cols=12, flow_order="dr").scale(1.25).center().to_edge(LEFT).shift(DOWN)

        self.add(self.title)
        self.add(self.label)
        self.add(self.grid)
        self.wait()

        self.HIGHLIGHT = YELLOW_D

    def writeSummary(self, summary):
        self.summary = summary
        self.play(Write(self.summary.next_to(self.title, DOWN, buff=0.75))) 
        self.wait()

    def highlight(self, mob):
        return mob.animate.set_color(self.HIGHLIGHT)

    def unhighlight(self, mob):
        return mob.animate.set_color(WHITE)
    
    def cleanup(self):
        self.play(FadeOut(self.summary))
        self.wait()
