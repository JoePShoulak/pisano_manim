from manim import *

class TenFivePattern(Scene):
    def construct(self):
        self.title = Text("Patterns", font_size=89).to_edge(UP)

        self.label = MathTex("P(", "10", ",", "5", ")")
        self.label.set_color_by_tex("10", RED).set_color_by_tex("5", ORANGE)
        self.label.scale(1.875).to_edge(UL)

        residuals = [0, 1]
        while len(residuals) != 60:
            residuals += [(residuals[-2] + residuals[-1]) % 10]

        self.grid = VGroup(*[Tex(n) for n in residuals])
        self.grid.arrange_in_grid(rows=5, cols=12, flow_order="dr").scale(1.25).center().to_edge(LEFT).shift(DOWN)

        self.add(self.title)
        self.add(self.label)
        self.add(self.grid)

        self.HIGHLIGHT = YELLOW_D

    def highlight(self, mob):
        return mob.animate.set_color(self.HIGHLIGHT)

    def unhighlight(self, mob):
        return mob.animate.set_color(WHITE)