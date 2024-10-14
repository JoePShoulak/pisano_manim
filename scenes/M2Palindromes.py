from manim import *
from templates import *

class M2Palindromes(PisanoScene):
    def construct(self):
        super().construct()

        def isPalindrome(tex):
            arr = [t.get_tex_string() for t in tex]
            return arr == arr[::-1]

        def makeGrid(m):
            grid = self.makeGrid(m, 2)
            grid.scale(1.25 if len(grid) < 30 else 0.9)
            return grid.center().shift(DOWN*0.5)

        def demo(m):
            if not self.grid:
                self.grid = makeGrid(m)
                self.label = self.makeGridLabel(m, 2)
                self.play(Write(self.grid), Write(self.label))
            else:
                self.play(
                    Transform(self.grid, makeGrid(m)),
                    Transform(self.label, self.makeGridLabel(m, 2))
                )
                self.remove(self.grid)
                self.grid = makeGrid(m)
                self.add(self.grid)
            self.wait()

            rows = [VGroup(*[i for i in self.grid[j::2]]) for j in range(2)]
            palindromes = [{"mobj": rows[1], "color": self.HIGHLIGHT}]
            subLength = int(len(rows[0])/2-1)
            topLeft = rows[0][1:subLength+1]
            topRight = rows[0][subLength+2:]
            if isPalindrome(topLeft) and isPalindrome(topRight) and len(topLeft) >= 3:
                palindromes += [
                    {"mobj": topLeft, "dir": UP, "color": ORANGE},
                    {"mobj": topRight, "dir": UP, "color": RED}
                ]
            self.palindromeAnim(palindromes)
            self.wait()

        title = Text("Patterns", font_size=89).to_edge(UP)
        subtitle = Tex("Just so many ", "palindromes", font_size=55)
        subtitle.to_edge(UP, buff=2)
        subtitle[1].set_color_by_gradient(self.HIGHLIGHT, RED)
        with self.voiceover(
            """Okay, so when I said another pattern was my favorite pattern, that was specifically in the ten-five Pisano array."""
        ):
            self.play(Write(title))
        with self.voiceover(
            """This is probably my favorite pattern over all. We'll consider arrays of a bunch of different moduli, but all of height two."""
        ):
            self.play(Write(subtitle))

        self.grid, self.label = VGroup(), VGroup()

        with self.voiceover("With all the ones I've tested, the bottom row is a palindrome. I haven't proven this yet, but how exciting would that be?"):
            demo(3)
            demo(4)

        with self.voiceover(
            """For some of them, the top row consists of two palindromes seperated by zeroes.
            Again, I haven't figured out exactly when and why these happen, but I'd love to know.
            I think this is a bit more fun to watch than talk about, so let's just enjoy for a moment."""
        ):
            for m in range(5, 20):
                demo(m)
            self.wait()

        self.play(
            FadeOut(self.grid),
            FadeOut(self.label),
            FadeOut(subtitle),
            FadeOut(title)
        )
        self.wait()
