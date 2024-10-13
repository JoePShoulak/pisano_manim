from manim import *
from templates import *

class M2Palindromes(PisanoScene):
    def construct(self):
        super().construct()

        def makeGrid(m):
            return self.makeGrid(m, 2).scale(1.25).center().shift(DOWN*0.5)

        def demo(m):
            if not self.grid:
                self.grid = makeGrid(m)
                self.label = self.makeGridLabel(m, 2)
                self.play(Write(self.grid), Write(self.label))
            else:
                self.play(Transform(self.grid, makeGrid(m)), Transform(self.label, self.makeGridLabel(m, 2)))
                self.remove(self.grid)
                self.grid = makeGrid(m)
                self.add(self.grid)
            self.wait()

            rows = [VGroup(*[i for i in self.grid[j::2]]) for j in range(2)]
            palindromes = [{"mobj": rows[1]}]
            subLength = int(len(rows[0])/2-1)
            if subLength >= 3:
                palindromes += [{"mobj": rows[0][1:subLength+1], "dir": UP}]
                palindromes += [{"mobj": rows[0][subLength+2:], "dir": UP}]
            self.palindromeAnim(palindromes)
            self.wait()

        title = Text("Patterns", font_size=89).to_edge(UP)
        subtitle = Tex("Just so many ", "palindromes", font_size=55).to_edge(UP, buff=2)
        subtitle[1].set_color_by_gradient(self.HIGHLIGHT, RED)
        self.play(Write(title))
        self.play(Write(subtitle))

        self.grid, self.label = VGroup(), VGroup()

        for m in range(3, 20):
            demo(m)
        self.wait()

        self.play(FadeOut(self.grid), FadeOut(self.label), FadeOut(subtitle), FadeOut(title))
        self.wait()
