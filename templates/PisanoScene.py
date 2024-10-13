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