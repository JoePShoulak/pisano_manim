from manim import *
from templates import *

class Fibonacci(Scene):
    def construct(self):
        # Title and definition of the Fibonacci numbers
        title = Text("Fibonacci Numbers", font_size=89).to_edge(UP)
        subtitle = MathTex(r"f_{0} = 0, \ f_{1} = 1, \ f_{n}=f_{n-1}+f_{n-2}", font_size=55)
        subtitle.to_edge(UP, buff=2)
        self.wait()
        self.play(Write(title))
        self.play(Write(subtitle))

        self.next_section("FIBONACCI")
        # Drawing the Fibonacci equations
        vals = [0,1,1]
        eqns = VGroup(MathTex(*r"{:.0f}  +  {:.0f}  =  {:.0f}".format(*vals).split("  ")))
        for i in range(7):
            vals.append(vals[1]+vals[2])
            vals.pop(0)
            eqn = MathTex(*r"{:.0f}  +  {:.0f}  =  {:.0f}".format(*vals).split("  "))
            eqn.next_to(eqns[-1],DOWN)
            eqn.shift((eqns[-1][3].get_bottom()[0]-eqn[1].get_top()[0])*RIGHT)
            eqns += eqn
        eqns.next_to(subtitle, DOWN)
        self.play(Write(eqns))
        self.wait()
        
        self.next_section("REDUCTION")
        # Reducing the equations to the right hand side
        self.play(*[eqn.animate.become(eqn[4]) for eqn in eqns])
        self.wait()

        # Aligning everything in one row with the numbers and elipsis
        eqns.insert(0, MathTex("1").next_to(eqns[0], LEFT))
        eqns.insert(0, MathTex("0").next_to(eqns[0], LEFT))
        eqns += MathTex(r"\ldots").next_to(eqns[-1], RIGHT)
        self.play(
            AnimationGroup(Write(eqns[0]), Write(eqns[1]), Write(eqns[-1])),
            AnimationGroup(eqns.animate.arrange(RIGHT).shift(UP), FadeOut(subtitle)),
            lag_ratio=0.5
        )
        self.wait()

        self.next_section("MODULUS")
        # New definition at the top of the screen
        subtitle = Tex("A number modulus 10 is the one's digit", font_size=55)
        subtitle.to_edge(UP, buff=2)
        self.play(Write(subtitle))
        self.wait()

        # Create our modulus numbers
        modEqns = VGroup()
        for eqn in eqns:
            nEq = MathTex(int((eqn if len(eqn) == 1 else eqn[4]).get_tex_string()) % 10)
            modEqns += nEq.next_to(eqn, DOWN, buff=2)
        modEqns += MathTex(r"\ldots").next_to(modEqns[-1], RIGHT).align_to(eqns[-1], RIGHT)

        # Make an arrow with a label to be clear what we're doing
        arrow = Arrow(start=UP, end=DOWN).next_to(modEqns[0], UP)
        arrowGroup = VGroup(arrow, MathTex(r"\bmod_{10}"))
        arrowGroup.add_updater(lambda l : l.next_to(arrow, RIGHT))

        # Animate the taking of the modulus
        self.play(Write(modEqns[0]), Write(arrowGroup))
        self.wait()
        for eqn in modEqns[1:-1]:
            self.play(
                AnimationGroup(Write(eqn)),
                AnimationGroup(arrow.animate.next_to(eqn, UP), run_time=0.33),
                lag_ratio=0.5
            )
        self.play(Write(modEqns[-1]), FadeOut(arrowGroup))
        self.wait()

        # Fade out the old numbers and shift these up; left shift is to be centered way later on
        self.play(
            modEqns.animate.arrange(RIGHT).to_edge(UP, buff=3).shift(LEFT*0.12590103),
            FadeOut(eqns)
        )
        self.wait()

        self.next_section("OUTRO")
        self.play(
            Transform(title, Text("Pisano Arrays", font_size=89).to_edge(UP)),
            FadeOut(subtitle))
        self.wait()

class Pisano(Scene):
    def construct(self):
        # Recreate everything from the last scene
        pisanoTitle = Text("Pisano Arrays", font_size=89).to_edge(UP)
        subtitle = MathTex(r"\text{The Fibonacci numbers} \bmod_", "{10}",
                           r" \text{ repeat every 60, so } \pi(", "10", ")=60", font_size=34)
        subtitle.to_edge(UP, buff=2).set_color_by_tex("10", RED)
        eqns = VGroup(*[MathTex(n) for n in [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, r"\ldots"]])
        eqns.arrange(RIGHT).to_edge(UP, buff=3).shift(LEFT*0.12590103)
        self.add(pisanoTitle)
        self.add(eqns)
        self.play(Write(subtitle))
        self.wait(2)

        self.next_section("PISANO SEQUENCE 10")
        # Remove the dots
        dots = eqns[-1]
        eqns.remove(dots)

        # Write in the rest of the numbers
        for num in [5, 9, 4, 3, 7, 0, 7, 7, 4, 1,
                    5, 6, 1, 7, 8, 5, 3, 8, 1, 9,
                    0, 9, 9, 8, 7, 5, 2, 7, 9, 6,
                    5, 1, 6, 7, 3, 0, 3, 3, 6, 9,
                    5, 4, 9, 3, 2, 5, 7, 2, 9, 1]:
            eqns.add(MathTex(num).next_to(eqns[-1], RIGHT))
        self.play(FadeOut(dots), Write(eqns[10:]))
        self.wait()
        
        # Fade out the pisano period mention
        self.play(FadeOut(subtitle))
        self.wait()

        self.next_section("P(10,5) DEFINITION")
        # Throw up a new subtitile for the occasion
        subtitle = Tex("Pisano Arrays need a ", "modulus", " and a ", "height", font_size=55)
        subtitle.to_edge(UP, buff=2).set_color_by_tex("modulus", RED)
        subtitle.set_color_by_tex("height", ORANGE)
        self.play(Write(subtitle))

        # First column
        self.play(
            *[eqns[i].animate.next_to(eqns[0], DOWN, buff=0.25+max(0.625*(i-1), 0)) for i in range(1, 5)]
        )

        # Rest of the columns
        for j in range (1, 12):
            self.play(
                 # Move the next 5 into a column
                *[eqns[i].animate.next_to(eqns[i-5], RIGHT) for i in range(5*j, 5*(j+1))],
                 # Move the rest down to be columns on the next round
                *[eqns[i].animate.move_to(eqns[i-4].get_center()) for i in range(5*(j+1), len(eqns))]
            )
        self.wait()

        # Draw the brackets and defining left hand side
        lBrack = MathTex("[").scale(6).next_to(eqns, LEFT)
        lHDef = MathTex("P(", "m", ",", "h", ")", "=").scale(1.25).next_to(lBrack, LEFT)
        lHDef.set_color_by_tex("m", RED).set_color_by_tex("h", ORANGE)
        rBrack = MathTex("]").scale(6).next_to(eqns, RIGHT)
        self.play(
            Write(lHDef[0]), Write(lHDef[2]), Write(lHDef[4:]),
            FadeOut(subtitle[0]), Transform(subtitle[1], lHDef[1]),
            FadeOut(subtitle[2]), Transform(subtitle[3], lHDef[3]),
            Write(lBrack),
            Write(rBrack),
        )
        self.wait()

        lHDef = VGroup(lHDef[0], subtitle[1], lHDef[2], subtitle[3], lHDef[4], lHDef[5])

        # Update the definition to show the correct numbers
        lHDefNums = MathTex("P(", "10", ",", "5", ")", "=").move_to(lHDef.get_center())
        lHDefNums.set_color_by_tex("10", RED).set_color_by_tex("5", ORANGE).scale(1.25)
        self.play(lHDef.animate.become(lHDefNums))
        self.wait()

        self.next_section("OUTRO")
        # Prep for scene change
        gridLabel = VGroup(lHDef[0], subtitle[1], lHDef[2], subtitle[3], lHDef[4])
        patternTitle = Text("Patterns", font_size=89).to_edge(UP)
        self.play(
            gridLabel.animate.scale(1.5).to_edge(UL),
            Transform(pisanoTitle, patternTitle),
            FadeOut(lHDef[5]), FadeOut(lBrack), FadeOut(rBrack)
        )
        self.play(
            eqns.animate.arrange_in_grid(rows=5,
                                         cols=12,
                                         flow_order="dr").scale(1.25).center().to_edge(LEFT).shift(DOWN)
        )
        self.wait()

class TenFiveDiagPalindrome(TenFivePattern):
    def construct(self):
        super().construct()
        self.writeSummary(
            Tex("Down-Right Diagonals (below the top row) form ",
                              "palindromes",
                              font_size=34).set_color_by_tex("palindromes", self.HIGHLIGHT)
        )
        for i in range(12):
            self.playDemo(i, first=i==0, last=i==11)
        self.cleanup()

    def playDemo(self, slice, first=False, last=False):
        ### HELPERS ###
        def makeDemo(): # Make the 4 numbers we'll be moving around
            demo = VGroup(*[Tex(eqn.get_tex_string(), color=self.HIGHLIGHT) for eqn in getSelection(slice)])
            return demo.scale(2).arrange(RIGHT, buff=1.0).next_to(self.grid, RIGHT).to_edge(RIGHT, buff=1.5)

        def getSelection(n): # Get those 4 mobs from the source grid
            return VGroup(*[self.grid[(1+6*i+5*n) % 60] for i in range(4)])

        ### ANIMATIONS ###
        introAnims = [self.highlight(getSelection(slice))] # highlight the new set
        copy = makeDemo() # make a copy ahead of time
        if first:
            # if this is our first animation, hide the demo but in the right position
            self.demo = makeDemo().scale(0)
        else:
            # otherwise, unhighlight the last selection
            introAnims += [self.unhighlight(getSelection(slice-1))]
        introAnims += [self.demo.animate.become(makeDemo())] # become the current selection
        self.play(*introAnims) # play all our intro animations
        if first: # only demo the first reversal
            # split the original and the copy
            self.play(self.demo.animate.shift(UP), copy.animate.shift(DOWN)) 
            # invert the position of every letter of the copy
            self.play(*[copy[i].animate.move_to(copy[len(copy)-1-i]) for i in range(len(copy))]) 
            # re-overlay the two copies to show they're identical
            self.play(self.demo.animate.shift(DOWN), copy.animate.shift(UP)) 
            # kill the copy quick
            self.play(FadeOut(copy), run_time=0.01) 
        elif last: # if we're done, fade out the demo and unhighlight the last text
            self.play(FadeOut(self.demo), self.unhighlight(getSelection(slice)))
        self.wait(0.5)
        
class TenFiveDiagSum(TenFivePattern):
    def construct(self):
        super().construct()
        s = Tex("Down-Left Diagonals (below the top row) form ",
                "sums", " pointing inward", font_size=34)
        s[1].set_color_by_gradient(self.HIGHLIGHT, RED)
        self.writeSummary(s)
        for i in range(12):
            self.playDemo(i, first=i==0, last=i==11)
        self.cleanup()

    def playDemo(self, slice, first=False, last=False):
        ### HELPERS ###
        def makeEquation(a, b, mod=False, startColor=self.HIGHLIGHT):
            [eq, sum] = ["=", a+b] if not mod else [r"\Rightarrow", (a+b)%10]
            return MathTex(a, "+", b, eq, sum).set_color_by_gradient(startColor, ORANGE)

        def getSelection(n): # Get those 4 mobs from the source grid
            return VGroup(*[self.grid[(4+4*i+5*n) % 60] for i in range(4)])
                
        def makeDemo(): # Make the 4 numbers we'll be moving around
            sel = [int(tex.get_tex_string()) for tex in getSelection(slice)]
            demo = VGroup(
                makeEquation(sel[3], sel[2], startColor=RED), makeEquation(sel[0], sel[1])
            )
            demo.scale(2).arrange(DOWN).next_to(self.grid, RIGHT).to_edge(RIGHT, buff=1.5)

            def demoUpdater(demo):
                k = demo[0].get_left()[0] < demo[1].get_left()[0]
                demo[1-k].align_to(demo[k], LEFT)

            return demo.add_updater(demoUpdater)
        
        ### ANIMATIONS ###
        introAnims = [getSelection(slice).animate.set_color_by_gradient(self.HIGHLIGHT, RED)]
        if first:
            # if this is our first animation, hide the demo but in the right position
            self.demo = makeDemo().scale(0)
        else:
            # otherwise, unhighlight the last selection
            introAnims += [self.unhighlight(getSelection(slice-1))]
        introAnims += [self.demo.animate.become(makeDemo())] # become the current selection
        self.play(*introAnims) # play all our intro animations
        sel = [int(tex.get_tex_string()) for tex in getSelection(slice)]
        reduceAnim = []
        if sel[3]+sel[2] >= 10:
            newEq = makeEquation(sel[3], sel[2], mod=True, startColor=RED)
            newEq.scale(2).move_to(self.demo[0].get_center()).align_to(self.demo[0], LEFT)
            reduceAnim.append(self.demo[0].animate.become(newEq))
        if sel[0]+sel[1] >= 10:
            newEq = makeEquation(sel[0], sel[1], mod=True)
            newEq.scale(2).move_to(self.demo[1].get_center()).align_to(self.demo[1], LEFT)
            reduceAnim.append(self.demo[1].animate.become(newEq))
        if reduceAnim:
            self.wait(0.5)
            self.play(*reduceAnim)

        if first:
            self.wait()
        elif last: # if we're done, fade out the demo and unhighlight the last text
            self.play(FadeOut(self.demo), self.unhighlight(getSelection(slice)))
        self.wait(0.5)
        
class TenFiveRightAngle(TenFivePattern):
    def construct(self):
        super().construct()
        self.writeSummary(Tex("Right Angles at the bottom (\"pointing\" down-right) ",
                              "repeat", font_size=34).set_color_by_tex("repeat", self.HIGHLIGHT))
        for i in range(12):
            self.playDemo(i, first=i==0, last=i==11)
        self.cleanup()

    def playDemo(self, slice, first=False, last=False):
        ### HELPERS ###
        def makeDemo(): # Make the 4 numbers we'll be moving around
            demo = VGroup(*getSelection(slice)).copy().scale(2/1.5)
            for d in demo[:-1]:
                d.color = self.HIGHLIGHT
            demo[3].next_to(demo[2], RIGHT)
            demo[4].next_to(demo[3], RIGHT)
            demo[1].next_to(demo[4], UP)
            demo[0].next_to(demo[1], UP)
            return demo.next_to(self.grid, RIGHT).to_edge(RIGHT, buff=3)

        def getSelection(n): # Get those 4 mobs from the source grid
            return VGroup(
                *[self.grid[(12+i+5*n) % 60] for i in range(2)],
                *[self.grid[(4+5*(1-i)+5*n) % 60] for i in range(2)],
                self.grid[(14+5*n) % 60]
            )
        
        ### ANIMATIONS ###
        introAnims = [self.highlight(getSelection(slice)[:-1])] # highlight the new set
        if first:
            self.demo = makeDemo().scale(0)
        else:
            introAnims += [self.unhighlight(getSelection(slice-1)[i]) for i in [0, 1, 3,]]
        introAnims += [self.demo.animate.become(makeDemo())] # become the current selection
        self.play(*introAnims) # play all our intro animations
        if first:
            self.wait()
            miniGrid = VGroup(*self.demo[:-1])
            self.play(
                miniGrid.animate.arrange_in_grid(rows=2),
                FadeOut(self.demo[-1], scale=0)
            )
            self.demo[-1].scale(0)
        elif last: # if we're done, fade out the demo and unhighlight the last text
            self.play(FadeOut(self.demo), self.unhighlight(getSelection(slice)))
        self.wait(0.5)
        