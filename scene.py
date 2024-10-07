from manim import *

hD, vD = 0.75, 0.75
hOff, vOff = -3, -1.5

def fibLines(num):
    a, b = 0, 1
    i = 0

    while i < num:
        yield f"{a}+{b}={a+b}"
        a, b = b, a+b
        i += 1

def alignLines(eq, i):
    return eq.shift(RIGHT * hD * (i+hOff)).shift(DOWN * vD * (i+vOff))

class Fibonacci(Scene):
    def construct(self):
        # Start with title already on screen, and draw the defintition of the Fibonacci numbers
        title = Text("Fibonacci Numbers", font_size=89).to_edge(UP)
        definition = MathTex(r"f_{0} = 0, \ f_{1} = 1, \ f_{n}=f_{n-1}+f_{n-2}", font_size=55).shift(UP * 2)
        self.add(title)
        self.play(Write(definition))

        # Setup all our equations to be drawn
        eqs = []
        reducedEqs = []
        for i, eq in enumerate(fibLines(6)):
            eqs += alignLines(Tex(eq, font_size=55), i)
            reducedEqs += alignLines(Tex(eq.split('=')[1]), i)

        # Draw all the equations on the screen to begin our Fibonacci introduction
        for eq in eqs:
            self.play(Write(eq))

        self.wait(1)

        # reduce from equations to the right hand size numbers
        reduceAnim = list(map(lambda i: Transform(eqs[i], reducedEqs[i]), range(len(eqs))))
        self.play(*reduceAnim)

        # align all our staggered numbers into one clean row
        alignAnim = list(map(lambda i: eqs[i+1].animate.align_to(eqs[0], UP), range(len(eqs)-1)))
        # add the numbers we lopped off the left, and an elipsis on the right
        p1 = Tex("1", font_size=55).next_to(eqs[0], LEFT, buff=hD*2/3) # buff is not correct
        p0 = Tex("0", font_size=55).next_to(p1, LEFT, buff=hD*2/3) # buff is not correct
        cdots = Tex(r"\ldots", font_size=55).next_to(eqs[-1], RIGHT, buff=hD*2/3).align_to(p0, UP).shift(DOWN * 0.25) # This is also not correctly aligned
        eqs = [p0, p1] + eqs
        self.play(
            AnimationGroup(
                AnimationGroup(*alignAnim),
                AnimationGroup(Write(p0), Write(p1), Write(cdots)),
                lag_ratio=0.5
            )
        )

        modEqs = []
        arrow = MathTex(r"\downarrow", font_size=55).next_to(eqs[0], DOWN)

        for i, eq in enumerate(eqs):
            s = eq.get_tex_string()
            newEq = MathTex(int(s.split('=')[1] if s.find('=') != -1 else s)% 10, font_size=55)
            if i == 0:
                newEq.next_to(arrow, DOWN)
            else:
                newEq.next_to(modEqs[-1], RIGHT).align_to(eq, RIGHT)

            modEqs += [newEq]
            self.play(
                AnimationGroup(
                    Write(arrow) if i == 0 else arrow.animate.align_to(eq, RIGHT),
                    Write(newEq),
                    lag_ratio=0.5
                )
            )

        mdots = Tex(r"\ldots", font_size=55).next_to(modEqs[-1], RIGHT, buff=hD*2/3).shift(DOWN * 0.25) # This is also not correctly aligned
        self.play(                
            AnimationGroup(
                    FadeOut(arrow),
                    Write(mdots),
                    lag_ratio=0.5
                ))

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

        pArr.scale(0.75)

        self.play(Create(pArr, run_time=3))
        self.wait()

class Test(Scene):
    def construct(self):
        title = Text("Pisano Arrays", font_size=89).to_edge(UP, buff=0.5)

        self.play(Write(title, run_time=2))
        self.wait()
