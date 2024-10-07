from manim import *

def fibLines(num):
    a, b = 0, 1
    i = 0

    while i < num:
        yield f"{a}+{b}={a+b}"
        a, b = b, a+b
        i += 1

class Fibonacci(Scene):
    def construct(self):
        title = Text("Fibonacci Numbers", font_size=89).shift(UP * 3)
        definition = MathTex(r"f_{0} = 0, \ f_{1} = 1, \ f_{n}=f_{n-1}+f{n-2}", font_size=55).shift(UP * 2)
        self.add(title)
        self.add(definition)

        hD, vD = 0.75, 0.75
        hOff, vOff = -3, -1.5

        lines = []
        for i, line in enumerate(fibLines(6)):
            lines += Tex(line, font_size=55).shift(RIGHT * hD * (i+hOff)).shift(DOWN * vD * (i+vOff))

        for line in lines:
            self.play(Create(line))

class Pisano(Scene):
    def construct(self):
        title = Text("Pisano Arrays", font_size=89).shift(UP * 3)
        self.add(title)

        pArr = Matrix([
            [0, 5, 5, 0, 5, 5, 0, 5, 5, 0, 5, 5],
            [1, 8, 9, 7, 6, 3, 9, 2, 1, 3, 4, 7],
            [1, 3, 4, 7, 1, 8, 9, 7, 6, 3, 9, 2],
            [2, 1, 3, 4, 7, 1, 8, 9, 7, 6, 3, 9],
            [3, 4, 7, 1, 8, 9, 7, 6, 3, 9, 2, 1]])

        pArr.scale(0.5)

        self.play(Create(pArr))

