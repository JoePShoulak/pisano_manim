from manim import *
from templates import *

from Fibonacci import Fibonacci
from Pisano import Pisano
from M2Palindromes import M2Palindromes

class FibonacciScene(Fibonacci):
    pass

class PisanoScene(Pisano):
    pass

class TenFiveDiagPalindrome(TenFivePattern):
    def construct(self):
        super().construct()
        self.writeSummary(Tex("Down-Right Diagonals (below the top row) form ", "palindromes", font_size=34).set_color_by_tex("palindromes", self.HIGHLIGHT))
        for i in range(12):
            self.playDemo(i)
        self.cleanup()

    def playDemo(self, index):
        def makeDemo():
            demo = VGroup(*[Tex(eqn.get_tex_string(), color=self.HIGHLIGHT) for eqn in getSelection(index)])
            return demo.scale(2).arrange(RIGHT, buff=1.0).next_to(self.grid, RIGHT).to_edge(RIGHT, buff=1.5)

        def getSelection(n):
            return self.getSelection(1, 6, 4, n)
        
        first = not self.demo

        introAnims = [self.highlight(getSelection(index))] # highlight the new set
        if first:
            self.demo = makeDemo().scale(0) # if this is our first animation, hide the demo but in the right position
        else:
            introAnims += [self.unhighlight(getSelection(index-1))] # otherwise, unhighlight the last selection
        introAnims += [self.demo.animate.become(makeDemo())] # become the current selection
        self.play(*introAnims) # play all our intro animations
        if first: # only demo the first reversal
            self.palindromeAnim({"mobj": self.demo, "sym": True})
        self.wait(0.5)
        
class TenFiveDiagSum(TenFivePattern):
    def construct(self):
        super().construct()
        s = Tex("Down-Left Diagonals (below the top row) form ", "sums", " pointing inward", font_size=34)
        s[1].set_color_by_gradient(self.HIGHLIGHT, RED)
        self.writeSummary(s)
        for i in range(2):
        # for i in range(12):
            self.playDemo(i)
        self.cleanup()

    def playDemo(self, index):
        def getSelection(n):
            return self.getSelection(4, 4, 4, n)
                
        def makeDemo():
            sel = [int(tex.get_tex_string()) for tex in getSelection(index)]
            demo = VGroup(
                self.makeEquation(sel[3], sel[2]).set_color_by_gradient(RED, ORANGE),
                self.makeEquation(sel[0], sel[1], reverse=True).set_color_by_gradient(self.HIGHLIGHT, ORANGE))
            demo.scale(2).arrange(DOWN).next_to(self.grid, RIGHT, buff=0.5)

            def demoUpdater(demo):
                demo[1].align_to(demo[0][2], LEFT)
                demo[1][2:].align_to(demo[0][-1], LEFT)

            return demo.add_updater(demoUpdater)
        
        def reducedAnim(n1, n2, i, color=self.HIGHLIGHT):
            newEq = self.makeEquation(n1, n2, mod=True, reverse=i==1).set_color_by_gradient(color, ORANGE)
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
                *list(reversed(self.getSelection(12, 1, 2, n))),
                *self.getSelection(4, 5, 2, n),
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
        def getSelection(n):
            return self.getSelection(1, 5, 3, n)
                
        def makeDemo(mod=False): 
            sel = [int(tex.get_tex_string()) for tex in getSelection(index)]
            return self.makeEquation(sel[0], sel[1], mod).scale(2).next_to(self.grid, RIGHT).to_edge(RIGHT, buff=1.5)

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

class M2PalindromesScene(M2Palindromes):
    pass
