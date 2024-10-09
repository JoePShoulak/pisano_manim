from manim import *
from templates import *

class Fibonacci(Scene):
    def construct(self):
        # Title and definition of the Fibonacci numbers
        title = Text("Fibonacci Numbers", font_size=89).to_edge(UP)
        subtitle = MathTex(r"f_{0} = 0, \ f_{1} = 1, \ f_{n}=f_{n-1}+f_{n-2}", font_size=55).next_to(title, DOWN)
        self.wait()
        self.play(Write(title))
        self.play(Write(subtitle))

        # Drawing the Fibonacci equations
        vals = [0,1,1]
        eqns = VGroup(
            MathTex(*r"{:.0f}  +  {:.0f}  =  {:.0f}".format(*vals).split("  "))
        )
        for i in range(7):
            vals.append(vals[1]+vals[2])
            vals.pop(0)
            eqn = MathTex(*r"{:.0f}  +  {:.0f}  =  {:.0f}".format(*vals).split("  "))
            eqn.next_to(eqns[-1],DOWN).shift((eqns[-1][3].get_bottom()[0]-eqn[1].get_top()[0])*RIGHT)
            eqns += eqn
        eqns.next_to(subtitle, DOWN)
        self.play(Write(eqns))
        self.wait(1)
        
        # Reducing the equations to the right hand side
        self.play(*[Transform(eqn, eqn[4]) for eqn in eqns])
        self.wait(1)

        # Aligning everything in one row with the numbers and elipsis
        eqns.insert(0, MathTex("1").next_to(eqns[0], LEFT))
        eqns.insert(0, MathTex("0").next_to(eqns[0], LEFT))
        eqns += MathTex(r"\ldots").next_to(eqns[-1], RIGHT)
        self.play(
            AnimationGroup(Write(eqns[0]), Write(eqns[1]), Write(eqns[-1])),
            AnimationGroup(eqns.animate.arrange(RIGHT).shift(UP), FadeOut(subtitle)),
            lag_ratio=0.5
        )
        self.wait(1)

        # New definition at the top of the screen
        subtitle = Tex("A number modulus 10 is the one's digit", font_size=55).next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(1)

        # Create out modulus numbers
        modBuff = 2.0
        modEqns = VGroup(
            *[MathTex(int(eqn.get_tex_string()) % 10).next_to(eqn, DOWN, buff=modBuff) for eqn in eqns[:2]],
            *[MathTex(int(eqn[4].get_tex_string()) % 10).next_to(eqn, DOWN, buff=modBuff) for eqn in eqns[2:-1]]
        )
        modEqns += MathTex(r"\ldots").next_to(modEqns[-1], RIGHT).align_to(eqns[-1], RIGHT)

        # Make an arrow with an operator to be clear what we're doing
        aro = Arrow(start=UP, end=DOWN).next_to(modEqns[0], UP)
        modArrow = VGroup(aro, MathTex(r"\bmod 10").next_to(aro, RIGHT))

        # Animate the taking of the modulus
        self.play(
            Write(modEqns[0]),
            Write(modArrow)
        )
        self.wait(1)
        for eqn in modEqns[1:-1]:
            self.play(
                AnimationGroup(Write(eqn), run_time=1.0),
                AnimationGroup(modArrow.animate.align_to(eqn, LEFT).shift(LEFT*0.25*(aro.get_right()[0] - aro.get_left()[0])), run_time=0.33),
                lag_ratio=0.5
            )
        self.play(Write(modEqns[-1]), FadeOut(modArrow))
        self.wait(1)

        # Fade out the old numbers and shift these up
        # Left shift is to be centered way later on
        self.play(modEqns.animate.arrange(RIGHT).next_to(subtitle, DOWN).shift(LEFT*0.12590103), FadeOut(eqns))
        self.wait(1)

        # Prep for scene change
        self.play(Transform(title, Text("Pisano Arrays", font_size=89).to_edge(UP)), FadeOut(subtitle))
        self.wait(1)

class Pisano(Scene):
    def construct(self):
        pisanoTitle = Text("Pisano Arrays", font_size=89).to_edge(UP)
        
        pisDef = Tex("Pisano Arrays need a ", "modulus", " and a ", "height", font_size=55).move_to([0, 2.03873432, 0])
        pisDef.set_color_by_tex("modulus", RED).set_color_by_tex("height", ORANGE)

        modEqns = VGroup(*[MathTex(n) for n in [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, r"\ldots"]])
        modEqns.arrange(RIGHT).next_to(pisDef, DOWN).shift(LEFT*0.12590103)

        self.add(pisanoTitle)
        self.add(modEqns)
        self.play(Write(pisDef))
        self.wait(1)

        # Replace the dots with the rest of the numbers extending offscreen
        self.play(modEqns.animate.shift(DOWN), FadeOut(modEqns[-1]))
        modEqns.remove(modEqns[-1])

        newNums = [5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]
        for num in newNums:
            mob = MathTex(num).next_to(modEqns[-1], RIGHT)
            modEqns.add(mob)

        self.play(Write(modEqns[10:]))
        self.wait(1)

        # Begin building the grid!
        # First column
        gridAnim = []
        for i in range(1, 5):
            gridAnim += [modEqns[i].animate.next_to(modEqns[0], DOWN, buff=0.25+max(0.625*(i-1), 0))]
        self.play(*gridAnim)

        # Rest of the columns
        for j in range (1, 12):
            # Move the next 5 into a column
            for i in range(5*j, 5*(j+1)):
                gridAnim += [modEqns[i].animate.next_to(modEqns[i-5], RIGHT)]
            # Move the rest down to be columns on the next round
            for i in range(5*(j+1), len(modEqns)):
                gridAnim += [modEqns[i].animate.move_to(modEqns[i-4].get_center())]
            self.play(*gridAnim)

        self.wait(1)

        # Draw the brackets and defining left hand side
        lBrack = MathTex("[").scale(6).next_to(modEqns, LEFT)
        lHDef = MathTex("P(", "m", ",", "h", ")", "=").scale(1.25).next_to(lBrack, LEFT).set_color_by_tex("m", RED).set_color_by_tex("h", ORANGE)
        rBrack = MathTex("]").scale(6).next_to(modEqns, RIGHT)
        self.play(
            Write(lHDef[0]), Write(lHDef[2]), Write(lHDef[4:]),
            FadeOut(pisDef[0]), Transform(pisDef[1], lHDef[1]), FadeOut(pisDef[2]), Transform(pisDef[3], lHDef[3]),
            Write(lBrack),
            Write(rBrack),
        )
        self.wait()

        lHDef = VGroup(lHDef[0], pisDef[1], lHDef[2], pisDef[3], lHDef[4], lHDef[5])

        # Update the definition to show the correct numbers
        lHDefNums = MathTex("P(", "10", ",", "5", ")", "=").move_to(lHDef.get_center())
        lHDefNums.set_color_by_tex("10", RED).set_color_by_tex("5", ORANGE).scale(1.25)
        self.play(lHDef.animate.become(lHDefNums))
        self.wait()

        # Prep for scene change
        gridLabel = VGroup(lHDef[0], pisDef[1], lHDef[2], pisDef[3], lHDef[4])
        patternTitle = Text("Patterns", font_size=89).to_edge(UP)
        self.play(
            gridLabel.animate.scale(1.5).to_edge(UL),
            Transform(pisanoTitle, patternTitle),
            FadeOut(lHDef[5]), FadeOut(lBrack), FadeOut(rBrack)
        )
        self.play(modEqns.animate.arrange_in_grid(rows=5, cols=12, flow_order="dr").scale(1.25).center().to_edge(LEFT).shift(DOWN))
        self.wait()

class TenFivePalindrome(TenFivePattern):
    def construct(self):
        super().construct()
        self.wait(1)

        # Write summary
        summary = Tex("Down-Right Diagonals (below the top row) form ", "palindromes", font_size=34).next_to(self.title, DOWN, buff=0.75)
        summary.set_color_by_tex("palindromes", self.HIGHLIGHT)
        self.play(Write(summary)) 
        self.wait(1)

        # Begin Demo
        self.palDemo = VGroup()
        for i in range(12):
            self.demo(i, first=i==0, last=i==11)
        self.wait(1)

        # Cleanup
        self.play(FadeOut(summary))
        self.wait(1)

    def demo(self, slice, first=False, last=False):
        def makeDemo(): # Make the 4 numbers we'll be moving around
            return VGroup(*[Tex(eqn.get_tex_string(), color=self.HIGHLIGHT) for eqn in getSelection(slice)]).scale(2).arrange(RIGHT, buff=1.0).next_to(self.grid, RIGHT).to_edge(RIGHT, buff=1.5)

        def getSelection(n): # Get those 4 mobs from the source grid
            return VGroup(*[self.grid[(1+6*i+5*n) % 60] for i in range(4)])

        introAnims = [self.highlight(getSelection(slice))] # highlight the new set (in a list to play later)
        palCopy = makeDemo() # make a copy ahead of time

        if first: self.palDemo = makeDemo().scale(0) # if this is our first animation, hide the demo but in the right position
        else: introAnims += [self.unhighlight(getSelection(slice-1))] # otherwise, unhighlight the last selection (in a list to play later)

        introAnims += [self.palDemo.animate.become(makeDemo())] # final entry here, morph into the new selection

        self.play(*introAnims) # play all our intro animations

        if first: # only demo the first reversal
            self.play( # split the original and the copy
                self.palDemo.animate.shift(UP),
                palCopy.animate.shift(DOWN)
            )
            self.play( # invert the position of every letter of the copy
                *[palCopy[i].animate.move_to(palCopy[len(palCopy)-1-i]) for i in range(len(palCopy))]
            )
            self.play( # re overlay the two copies to show they're identical
                self.palDemo.animate.shift(DOWN),
                palCopy.animate.shift(UP)
            )
            self.play(FadeOut(palCopy), run_time=0.01) # kill the copy quick
        elif last: # if we're done, fade out the demo and unhighlight the last text
            self.play(
                FadeOut(self.palDemo),
                self.unhighlight(getSelection(slice))
            )
        
        self.wait(0.5)

        return self.palDemo # return the demo so we can keep updating and passing it
        