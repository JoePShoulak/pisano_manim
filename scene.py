from manim import *
from templates import *

class Fibonacci(PisanoScene):
    def construct(self):
        # Title and definition of the Fibonacci numbers
        title = Text("Fibonacci Numbers", font_size=89).to_edge(UP)
        subtitle = MathTex(r"f_{0} = 0, \ f_{1} = 1, \ f_{n}=f_{n-1}+f_{n-2}", font_size=55)
        subtitle.to_edge(UP, buff=2)
        self.wait()
        self.play(Write(title))
        self.play(Write(subtitle))

        self.next_section("EQUATIONS")
        # Drawing the Fibonacci equations
        vals = [0,1,1]
        eqns = VGroup(MathTex(*r"{:.0f}  +  {:.0f}  =  {:.0f}".format(*vals).split("  ")))
        for i in range(7):
            vals.append(vals[1]+vals[2])
            vals.pop(0)
            eqn = MathTex(*r"{:.0f}  +  {:.0f}  =  {:.0f}".format(*vals).split("  "))
            eqn.next_to(eqns[-1],DOWN).shift((eqns[-1][3].get_bottom()[0]-eqn[1].get_top()[0])*RIGHT)
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
        subtitle = Tex("A number ", "modulus 10", " is the one's digit", font_size=55).to_edge(UP, buff=2)
        subtitle.set_color_by_tex("modulus 10", RED)
        self.play(Write(subtitle))
        self.wait()

        # Create our modulus numbers
        modEqns = VGroup(*[MathTex(int((eqn if len(eqn) == 1 else eqn[4]).get_tex_string()) % 10).next_to(eqn, DOWN, buff=2) for eqn in eqns[:-1]])
        modEqns += MathTex(r"\ldots").next_to(modEqns[-1], RIGHT).align_to(eqns[-1], RIGHT)

        # Make an arrow with a label to be clear what we're doing
        arrow = Arrow(start=UP, end=DOWN).next_to(modEqns[0], UP)
        arrowGroup = VGroup(arrow, MathTex(r"\bmod_{10}", color=RED).add_updater(lambda l : l.next_to(arrow, RIGHT)))

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
        self.play(modEqns.animate.arrange(RIGHT).to_edge(UP, buff=3).shift(LEFT*0.12590103), FadeOut(eqns))
        self.wait()

        self.next_section("OUTRO")
        self.play(Transform(title, Text("Pisano Arrays", font_size=89).to_edge(UP)), FadeOut(subtitle))
        self.wait()

class Pisano(PisanoScene):
    def construct(self):
        # Recreate everything from the last scene
        pisanoTitle = Text("Pisano Arrays", font_size=89).to_edge(UP)
        subtitle = MathTex(r"\text{The Fibonacci numbers} \bmod_", "{10}", r" \text{ repeat every 60, so } \pi(", "10", ")=60", font_size=34)
        subtitle.to_edge(UP, buff=2).set_color_by_tex("10", RED)
        modEqns = VGroup(*[MathTex(n) for n in [*self.pisanoSequence(10)[:10], r"\ldots"]])
        modEqns.arrange(RIGHT).to_edge(UP, buff=3).shift(LEFT*0.12590103)
        self.add(pisanoTitle)
        self.add(modEqns)
        self.play(Write(subtitle))
        self.wait(2)

        self.next_section("PISANO SEQUENCE 10")
        # Remove the dots
        dots = modEqns[-1]
        modEqns.remove(dots)

        # Write in the rest of the numbers
        for num in self.pisanoSequence(10)[10:]:
            modEqns.add(MathTex(num).next_to(modEqns[-1], RIGHT))
        self.play(FadeOut(dots), Write(modEqns[10:]))
        self.wait()
        
        # Fade out the pisano period mention
        self.play(FadeOut(subtitle))
        self.wait()

        self.next_section("P(10,5) DEFINITION")
        # Throw up a new subtitile for the occasion
        subtitle = Tex("Pisano Arrays need a ", "modulus", " and a ", "height", font_size=55)
        subtitle.to_edge(UP, buff=2).set_color_by_tex("modulus", RED).set_color_by_tex("height", ORANGE)
        self.play(Write(subtitle))
        self.wait(1)

        # First column
        self.play(*[modEqns[i].animate.next_to(modEqns[0], DOWN, buff=0.25+max(0.625*(i-1), 0)) for i in range(1, 5)])

        # Rest of the columns
        for j in range (1, 12):
            self.play(
                *[modEqns[i].animate.next_to(modEqns[i-5], RIGHT) for i in range(5*j, 5*(j+1))], # Move the next 5 into a column
                *[modEqns[i].animate.move_to(modEqns[i-4].get_center()) for i in range(5*(j+1), len(modEqns))] # Move the rest down to be columns on the next round
            )
        self.wait()

        # Draw the brackets and defining left hand side
        lBrack = MathTex("[").scale(6).next_to(modEqns, LEFT)
        lHDef = MathTex("P(", "m", ",", "h", ")", "=").scale(1.25).next_to(lBrack, LEFT).set_color_by_tex("m", RED).set_color_by_tex("h", ORANGE)
        rBrack = MathTex("]").scale(6).next_to(modEqns, RIGHT)
        self.play(
            Write(lHDef[0]), Write(lHDef[2]), Write(lHDef[4:]),
            FadeOut(subtitle[0]), Transform(subtitle[1], lHDef[1]), FadeOut(subtitle[2]), Transform(subtitle[3], lHDef[3]),
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
        self.play(modEqns.animate.arrange_in_grid(rows=5, cols=12, flow_order="dr").scale(1.25).center().to_edge(LEFT).shift(DOWN))
        self.wait()

class TenFiveDiagPalindrome(TenFivePattern):
    def construct(self):
        super().construct()
        self.writeSummary(Tex("Down-Right Diagonals (below the top row) form ", "palindromes", font_size=34).set_color_by_tex("palindromes", self.HIGHLIGHT))
        for i in range(12):
            self.playDemo(i)
        self.cleanup()

    def playDemo(self, index):
        def makeDemo(): # Make the 4 numbers we'll be moving around
            demo = VGroup(*[Tex(eqn.get_tex_string(), color=self.HIGHLIGHT) for eqn in getSelection(index)])
            return demo.scale(2).arrange(RIGHT, buff=1.0).next_to(self.grid, RIGHT).to_edge(RIGHT, buff=1.5)

        def getSelection(n):
            return VGroup(*[self.grid[(1+6*i+5*n) % 60] for i in range(4)])
        
        first = not self.demo

        introAnims = [self.highlight(getSelection(index))] # highlight the new set
        if first:
            self.demo = makeDemo().scale(0) # if this is our first animation, hide the demo but in the right position
        else:
            introAnims += [self.unhighlight(getSelection(index-1))] # otherwise, unhighlight the last selection
        introAnims += [self.demo.animate.become(makeDemo())] # become the current selection
        self.play(*introAnims) # play all our intro animations
        if first: # only demo the first reversal
            self.palindromeAnim(self.demo, sym=True)
        self.wait(0.5)
        
class TenFiveDiagSum(TenFivePattern):
    def construct(self):
        super().construct()
        s = Tex("Down-Left Diagonals (below the top row) form ", "sums", " pointing inward", font_size=34)
        s[1].set_color_by_gradient(self.HIGHLIGHT, RED)
        self.writeSummary(s)
        for i in range(12):
            self.playDemo(i)
        self.cleanup()

    def playDemo(self, index):
        def makeEquation(a, b, mod=False, startColor=self.HIGHLIGHT):
            [eq, sum] = ["=", a+b] if not mod else [r"\Rightarrow", (a+b)%10]
            return MathTex(a, "+", b, eq, sum).set_color_by_gradient(startColor, ORANGE)

        def getSelection(n):
            return VGroup(*[self.grid[(4+4*i+5*n) % 60] for i in range(4)])
                
        def makeDemo(): # Make the 4 numbers we'll be moving around
            sel = [int(tex.get_tex_string()) for tex in getSelection(index)]
            demo = VGroup(makeEquation(sel[3], sel[2], startColor=RED), makeEquation(sel[0], sel[1]))
            demo.scale(2).arrange(DOWN).next_to(self.grid, RIGHT).to_edge(RIGHT, buff=1.5)

            def demoUpdater(demo):
                k = demo[0].get_left()[0] < demo[1].get_left()[0]
                demo[1-k].align_to(demo[k], LEFT)

            return demo.add_updater(demoUpdater)
        
        def reducedAnim(n1, n2, i, color=self.HIGHLIGHT):
            newEq = makeEquation(n1, n2, mod=True, startColor=color)
            newEq.scale(2).move_to(self.demo[i].get_center()).align_to(self.demo[i], LEFT)
            return self.demo[i].animate.become(newEq)
        
        first = not self.demo

        introAnims = [getSelection(index).animate.set_color_by_gradient(self.HIGHLIGHT, RED)] # highlight the new set
        if first:
            self.demo = makeDemo().scale(0) # if this is our first animation, hide the demo but in the right position
        else:
            introAnims += [self.unhighlight(getSelection(index-1))] # otherwise, unhighlight the last selection
        introAnims += [self.demo.animate.become(makeDemo())] # become the current selection
        self.play(*introAnims) # play all our intro animations
        sel = [int(tex.get_tex_string()) for tex in getSelection(index)]
        reduceAnims = []
        if sel[3]+sel[2] >= 10:
            reduceAnims.append(reducedAnim(sel[3], sel[2], 0, RED))
        if sel[0]+sel[1] >= 10:
            reduceAnims.append(reducedAnim(sel[0], sel[1], 1))
        if reduceAnims:
            self.wait(0.5)
            self.play(*reduceAnims)
        if first:
            self.wait()
        self.wait(0.5)
        
class TenFiveRightAngle(TenFivePattern):
    def construct(self):
        super().construct()
        self.writeSummary(Tex("Right Angles at the bottom (\"pointing\" down-right) ", "repeat", font_size=34).set_color_by_tex("repeat", self.HIGHLIGHT))
        for i in range(12):
            self.playDemo(i)
        self.cleanup()

    def playDemo(self, index):
        def makeDemo():
            demo = VGroup(*getSelection(index)).copy().scale(2/1.5)
            for d in demo[:-1]:
                d.color = self.HIGHLIGHT
            demo[3].next_to(demo[2], RIGHT)
            demo[4].next_to(demo[3], RIGHT)
            demo[0].next_to(demo[4], UP)
            demo[1].next_to(demo[0], UP)
            return demo.next_to(self.grid, RIGHT).to_edge(RIGHT, buff=3)

        # This is kinda horrible, but it lets me arrange in grid how I want
        def getSelection(n):
            return VGroup(
                *[self.grid[(12+(1-i)+5*n) % 60] for i in range(2)],
                *[self.grid[(4+5*i+5*n) % 60] for i in range(2)],
                self.grid[(14+5*n) % 60]
            )
        
        first = not self.demo
        
        introAnims = [self.highlight(getSelection(index)[:-1])] # highlight the new set
        if first:
            self.demo = makeDemo().scale(0) # if this is our first animation, hide the demo but in the right position
        else:
            introAnims += [self.unhighlight(getSelection(index-1)[i]) for i in [0, 1, 2]] # otherwise, unhighlight the last selection
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
        self.wait(0.5)
        
class TenFiveFrequency(TenFivePattern):
    def construct(self):
        super().construct()
        self.writeSummary(Tex("Numbers of the same parity have the same ", "frequency", font_size=34).set_color_by_tex("frequency", self.HIGHLIGHT))
        for i in range(2):
            self.playDemo(i)
        self.cleanup()

    def playDemo(self, index):
        def getSelection(n):
            return VGroup(*list(filter(lambda t : int(t.get_tex_string()) == n, self.grid)))
        
        def makeDemo():
            demo = VGroup(*[Tex(f"\# of {index+2*i}s: {len(getSelection(index+2*i))}", color=self.HIGHLIGHT) for i in range(5)])
            return demo.scale(1.25).arrange(DOWN).next_to(self.grid, RIGHT).to_edge(RIGHT, buff=3)

        if self.demo:
            self.play(FadeOut(self.demo))
            self.wait(0.5)

        self.demo = makeDemo()
        color = RED if index else ORANGE

        for i in range(6):
            if i > 0:
                self.play(
                    self.highlight(self.demo[i-1], color),
                    self.highlight(getSelection(index+2*(i-1)), color)
                )
            if i < 5:
                self.play(Write(self.demo[i]), self.highlight(getSelection(index+2*i)))
            self.wait(0.5)
        self.wait(0.5)

class TenFiveLucas(TenFivePattern):
    def construct(self):
        super().construct()
        self.writeSummary(Tex("All rows but the top are... ", "the same", "?", font_size=55).set_color_by_tex("the same", self.HIGHLIGHT))

        # Prep the grid for manipulation
        rows = VGroup(*[VGroup(*[self.grid[i] for i in range(j,60+j, 5)]) for j in range(5)])
        self.play(self.grid.animate.center().shift(DOWN))
        self.wait()

        self.play(FadeOut(rows[0]), self.highlight(rows[1:]))
        self.wait()

        gridWidth = rows[1][1].get_bottom()[0] - rows[1][0].get_bottom()[0]
        # Extend the rows
        for row in rows[1:]:
            for i in range(10):
                b, c = int(row[0].get_tex_string()), int(row[1].get_tex_string())
                row.insert(0, Tex((c - b) % 10).scale(1.25).move_to(row[0].get_center()).shift(LEFT*gridWidth))
            for i in range(10):
                a, b = int(row[-2].get_tex_string()), int(row[-1].get_tex_string())
                row.add(Tex((a+b) % 10).scale(1.25).move_to(row[-1].get_center()).shift(RIGHT*gridWidth))
        newNumsAnim = []
        for row in rows[1:]:
            for i in [*range(0, 10), *range(22, 32)]: 
                newNumsAnim += [Write(row[i])]
        self.play(*newNumsAnim)
        self.wait()

        # Align the rows
        self.play(
            rows[2].animate.align_to(rows[1][27], RIGHT),
            rows[3].animate.align_to(rows[1][26], RIGHT),
            rows[4].animate.align_to(rows[1][28], RIGHT)
        )
        self.wait(1.5)
        self.play(
            rows[4].animate.align_to(rows[1], UP).set_color(WHITE),
            rows[3].animate.align_to(rows[1], UP).set_color(WHITE),
            rows[2].animate.align_to(rows[1], UP).set_color(WHITE),
            rows[1].animate.set_color(WHITE)
        )
        self.wait(3)

        # Cleanup
        self.play(Transform(rows, self.makeGrid()), FadeOut(self.summary))
        self.wait()
        
class TenFiveRowSum(TenFivePattern):
    def construct(self):
        super().construct()
        self.writeSummary(Tex("Rows also have a pattern with ", "sums", font_size=55).set_color_by_tex("sums", self.HIGHLIGHT))
        for i in range(12):
            self.playDemo(i)
        self.cleanup()

    def playDemo(self, index):
        def makeEquation(a, b, mod=False):
            [eq, sum] = ["=", a+b] if not mod else [r"\Rightarrow", (a+b)%10]
            return MathTex(a, "+", b, eq, sum).set_color(self.HIGHLIGHT)

        def getSelection(n):
            return VGroup(*[self.grid[(1+5*i+5*n) % 60] for i in range(3)])
                
        def makeDemo(mod=False): 
            sel = [int(tex.get_tex_string()) for tex in getSelection(index)]
            return makeEquation(sel[0], sel[1], mod).scale(2).next_to(self.grid, RIGHT).to_edge(RIGHT, buff=1.5)

        first = not self.demo
        
        introAnims = [getSelection(index).animate.set_color(self.HIGHLIGHT)] # highlight the new set
        if first:
            self.demo = makeDemo().scale(0) # if this is our first animation, hide the demo but in the right position
        else:
            introAnims += [self.unhighlight(getSelection(index-1)[0])] # otherwise, unhighlight the last selection
        introAnims += [self.demo.animate.become(makeDemo())] # become the current selection
        self.play(*introAnims) # play all our intro animations
        sel = [int(tex.get_tex_string()) for tex in getSelection(index)]
        if sel[0] + sel[1] >= 10:
            self.play(self.demo.animate.become(makeDemo(True).align_to(self.demo, LEFT)))
        if first:
            self.wait()
        self.wait(0.5)
        
class TenFiveTopRow(TenFivePattern):
    def construct(self):
        super().construct()
        self.writeSummary(Tex("The top row is all ", "5", "s and ", "0", "s", font_size=55).set_color_by_tex("5", self.HIGHLIGHT).set_color_by_tex("0", self.HIGHLIGHT))
        self.play(self.highlight(VGroup(*[self.grid[i] for i in range(0, 60, 5)])))
        self.wait(0.5)
        
        self.play(self.unhighlight(self.grid))
        gridFrame = VGroup(self.summary, self.grid, self.label)
        self.play(FadeOut(gridFrame), Transform(self.title, Tex("Proof: $f_{5n}=5k$", font_size=89).to_edge(UP)))
        self.wait()

        self.next_section("PROOF")
        reminder = MathTex(r"f_{n}=f_{n-1}+f_{n-2}", font_size=55).next_to(self.title, DOWN)
        self.play(Write(reminder))

        # Proof that F(5n) = 5k
        proof = MathTex(
            r"f_{5n} &= f_{5n-1} + f_{5n-2}\\",
            r"&= 2f_{5n-2} + f_{5n-3}\\",
            r"&= 3f_{5n-3} + 2f_{5n-4}\\",
            r"&= 5f_{5n-4} + 3f_{5n-5}\\",
            r"&= 5f_{5n-4} + 3f_{5(n-1)}\\",
            r"&= 5f_{5n-4} + 3 \times 5m\\",
            r"&= 5(f_{5n-4} + 3m)\\",
            r"&= 5k\\", font_size=34,
        ).next_to(reminder, DOWN)

        for line in proof:
            self.play(Write(line))

        self.wait(3)
        self.play(FadeOut(proof))

        # Proof that F(15n)=10k
        proof = VGroup(
            MathTex(
                r"f_{15n} &= f_{15n-1} + f_{15n-2}\\",
                r"&= 2f_{15n-2} + f_{15n-3}\\",
                r"&= 3f_{15n-3} + 2f_{15n-4}\\",
                r"&= 5f_{15n-4} + 3f_{15n-5}\\",
                r"&= 8f_{15n-5} + 5f_{15n-6}\\",
                r"&= 13f_{15n-6} + 8f_{15n-7}\\",
                r"&= 21f_{15n-7} + 13f_{15n-8}\\",
                r"&= 34f_{15n-8} + 21f_{15n-9}\\",
                r"&= 55f_{15n-9} + 34f_{15n-10}",
                font_size=34,
            ), MathTex(
                r"&= 89f_{15n-10} + 55f_{15n-11}\\",
                r"&= 144f_{15n-11} + 89f_{15n-12}\\",
                r"&= 233f_{15n-12} + 144f_{15n-13}\\",
                r"&= 377f_{15n-13} + 233f_{15n-14}\\",
                r"&= 610f_{15n-14} + 377f_{15n-15}\\",
                r"&= 610f_{15n-14} + 377f_{15(n-1)}\\",
                r"&= 610f_{15n-14} + 377 \times 10m\\",
                r"&= 10(61f_{15n-14} + 377m)\\",
                r"&= 10k", font_size=34,
            )
        ).arrange(RIGHT).next_to(reminder, DOWN)

        for line in proof:
            self.play(Write(line))

        self.wait(3)
        self.play(FadeOut(proof), FadeOut(self.title), FadeOut(reminder))
        self.wait()

class M2Palindromes(PisanoScene):
    def construct(self):
        def demo(m):
            arr = self.makeGrid(m, 2).scale(1.25).center()
            lbl = self.makeGridLabel(m, 2)

            if not self.grid:
                self.grid = arr
                self.label = lbl
                self.play(Write(self.grid), Write(self.label))
            else:
                self.play(Transform(self.grid, arr), Transform(self.label, lbl))
            self.wait()

            rows = [VGroup(*[i for i in self.grid[j::2]]) for j in range(2)]
            self.palindromeAnim(rows[1])
            self.wait()

        self.play(Write(Text("Patterns", font_size=89).to_edge(UP)))

        self.grid = VGroup()
        for m in range(3, 10):
            demo(m)
        self.wait()
