from manim import *
import math

hD, vD = 0.75, 0.75
hOff, vOff = -4, -1.5

def fibLines(num):
    a, b = 0, 1
    i = 0

    while i < num:
        yield f"{a}+{b}={a+b}"
        a, b = b, a+b
        i += 1

bigFont = 89
smallFont = 55

def alignLines(eq, i):
    return eq.shift(RIGHT * hD * (i+hOff)).shift(DOWN * vD * (i+vOff))

def smallTex(text):
    return Tex(text, font_size=smallFont)

def writeMany(*mobs):
    return [Write(i) for i in mobs]

class Fibonacci(Scene):
    def construct(self):
        # Start with title already on screen, and draw the defintition of the Fibonacci numbers
        title = Text("Fibonacci Numbers", font_size=bigFont).to_edge(UP)
        definition = MathTex(r"f_{0} = 0, \ f_{1} = 1, \ f_{n}=f_{n-1}+f_{n-2}", font_size=smallFont).next_to(title, DOWN)
        self.wait()
        self.play(Write(title))
        self.play(Write(definition))

        # Setup all our equations to be drawn
        eqs = []
        reducedEqs = []
        for i, eq in enumerate(fibLines(5)):
            eqs += alignLines(Tex(eq, font_size=smallFont), i)
            reducedEqs += alignLines(Tex(eq.split('=')[1], font_size=smallFont), i)

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
        p1 = smallTex("1").next_to(eqs[0], LEFT, buff=hD*2/3) # buff is not correct
        p0 = smallTex("0").next_to(p1, LEFT, buff=hD*2/3) # buff is not correct
        n1 = smallTex("13").next_to(eqs[-1], RIGHT, buff=hD*2/3).align_to(p0, UP)
        n2 = smallTex("21").next_to(n1, RIGHT, buff=hD*2/3).align_to(p0, UP)
        n3 = smallTex("34").next_to(n2, RIGHT, buff=hD*2/3).align_to(p0, UP)
        n4 = smallTex("55").next_to(n3, RIGHT, buff=hD*2/3).align_to(p0, UP)
        cdots = smallTex(r"\ldots").next_to(n4, RIGHT, buff=hD*2/3).align_to(p0, UP).shift(DOWN * 0.25) # This is also not correctly aligned
        eqs = [p0, p1] + eqs + [n1, n2, n3, n4]
        self.play(
            AnimationGroup(
                AnimationGroup(*alignAnim),
                AnimationGroup(*writeMany(p0, p1, n1, n2, n3, n4, cdots), FadeOut(definition)),
                lag_ratio=0.5
            )
        )

        self.wait(1)

        # Begin to show all the numbers mod 10
        modEqs = []
        arrow = MathTex(r"\downarrow", font_size=smallFont).next_to(eqs[0], DOWN)

        # Do this bit by bit
        for i, eq in enumerate(eqs):
            # Make our new equations
            s = eq.get_tex_string()
            newEq = MathTex(int(s.split('=')[1] if s.find('=') != -1 else s)% 10, font_size=smallFont)
            if i == 0:
                newEq.next_to(arrow, DOWN)
            else:
                newEq.next_to(modEqs[-1], RIGHT).align_to(eq, RIGHT)

            modEqs += [newEq]
            # Animate the new row plus one arrow moving to follow the action
            self.play(
                AnimationGroup(
                    Write(arrow) if i == 0 else arrow.animate.align_to(eq, RIGHT),
                    Write(newEq),
                    lag_ratio=0.5
                ), run_time=1.5-math.sin(i*2*math.pi/(2*len(eqs)))
            )

        # Draw the dots and fade out the arrow to leave everything in a nice state for now
        mdots = Tex(r"\ldots", font_size=smallFont).next_to(modEqs[-1], RIGHT, buff=hD*2/3) # This is also not correctly aligned
        self.play(                
            AnimationGroup(
                    FadeOut(arrow),
                    Write(mdots),
                    lag_ratio=0.5
                ))

        self.wait(1)

        # Psuedo-scene change
        newTitle = Text("Pisano Arrays", font_size=bigFont).to_edge(UP)
        clearAnim = [FadeOut(cdots), Transform(title, newTitle)]
        for eq in eqs:
            clearAnim += [FadeOut(eq)]
        self.play(*clearAnim)
        self.wait()

        # Clean up our sequence
        modGroup = VGroup(*modEqs)
        self.play(modGroup.animate.arrange(RIGHT).shift(LEFT*2.0), FadeOut(mdots))
        newNums = VGroup(*[MathTex(i) for i in [9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]]).arrange(RIGHT).next_to(modGroup, RIGHT)
        self.play(Write(newNums))

class Pisano(Scene):
    def construct(self):
        title = Text("Pisano Arrays", font_size=bigFont).shift(UP * 3)
        self.add(title)

        nums = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]
        numMobs = []
        for i, n in enumerate(nums):
            numMobs += [smallTex(n)]
            if i != 0:
                numMobs[i].next_to(numMobs[i-1], RIGHT)
            
        self.add(*numMobs)
        self.wait()

class Test(Scene):
    def construct(self):
        title = Text("Pisano Arrays", font_size=bigFont).to_edge(UP, buff=0.5)

        self.play(Write(title, run_time=2))
        self.wait()
