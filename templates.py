from manim import *

HIGHLIGHT = YELLOW_D

class PisanoScene(Scene):
    def construct(self):
        self.HIGHLIGHT = HIGHLIGHT

    def pisanoSequence(self, m):
        ps = [0, 1]
        while ps[-2:] != [1, 0]:
            ps.append((ps[-2] + ps[-1]) % m)
        return ps[:-1]
    
    def makeGrid(self, m, h):
        grid = VGroup(*[Tex(n) for n in self.pisanoSequence(m)])
        return grid.arrange_in_grid(rows=h, flow_order="dr")
    
    def makeGridLabel(self, m, h):
        m, h = str(m), str(h)

        label = MathTex("P(", m, ",", h, ")")
        label.set_color_by_tex(m, RED).set_color_by_tex(h, ORANGE)
        return label.scale(1.875).to_edge(UL)
    
    # TODO: Allow highlighting as well
    def palindromeAnim(self, mobjDict = {"mobj": VGroup()}):
        if type(mobjDict) == dict:
            mobjDict = [mobjDict]

        shiftAwayAnim = []
        for mobjItem in mobjDict:
            mobjItem["copy"] = mobjItem["mobj"].copy()
            shiftAwayAnim += [mobjItem["copy"].animate.shift(mobjItem.get("dir", DOWN))]
            if mobjItem.get("sym", False): shiftAwayAnim += [mobjItem["mobj"].animate.shift(-mobjItem.get("dir", DOWN))]
        self.play(*shiftAwayAnim)

        reverseAnim = []
        for mobjItem in mobjDict:
            reverseAnim += [
                mobjItem["copy"][i].animate.move_to(mobjItem["copy"][len(mobjItem["copy"])-1-i])
                for i in range(len(mobjItem["copy"]))
            ]
        self.play(*reverseAnim)

        shiftBackAnim = []
        for mobjItem in mobjDict:
            shiftBackAnim += [mobjItem["copy"].animate.shift(-mobjItem.get("dir", DOWN))]
            if mobjItem.get("sym", False): shiftBackAnim += [mobjItem["mobj"].animate.shift(mobjItem.get("dir", DOWN))]
        self.play(*shiftBackAnim)

        for mobjItem in mobjDict:
            self.remove(mobjItem["copy"])

class TenFivePattern(PisanoScene):
    def construct(self):
        super().construct()
        self.title = Text("Patterns", font_size=89).to_edge(UP)
        self.label = self.makeGridLabel(10, 5)
        self.summary = MathTex()
        self.demo = VGroup()
        self.grid = self.makeGrid()

        self.add(self.title)
        self.add(self.label)
        self.add(self.grid)
        self.wait()

    def makeGrid(self):
        return super().makeGrid(10, 5).scale(1.25).center().to_edge(LEFT).shift(DOWN)

    def makeEquation(self, a, b, mod=False):
        [eq, sum] = ["=", a+b] if not mod else [r"\Rightarrow", (a+b)%10]
        return MathTex(a, "+", b, eq, sum).set_color(self.HIGHLIGHT)

    def getSelection(self, offset, distance, r, n):
        return VGroup(*[self.grid[(offset+distance*i+5*n) % 60] for i in range(r)])

    def writeSummary(self, summary, wait_time=1):
        self.summary = summary
        self.play(Write(self.summary.next_to(self.title, DOWN, buff=0.75))) 
        
        if wait_time: self.wait(wait_time)

    def highlight(self, mob, color=HIGHLIGHT):
        return mob.animate.set_color(color)

    def unhighlight(self, mob):
        return self.highlight(mob, color=WHITE)
    
    def cleanup(self):
        self.play(FadeOut(self.summary), FadeOut(self.demo), self.unhighlight(self.grid))
        self.wait()
