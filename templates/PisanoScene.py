from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class PisanoScene(VoiceoverScene):
    def construct(self):
        self.HIGHLIGHT = YELLOW_D
        self.set_speech_service(
        AzureService(
            voice="en-US-AriaNeural",
            style="newscast-casual"
        )
        )
        
    def pisanoSequence(self, m):
        ps = [0, 1]
        while ps[-2:] != [1, 0]:
            ps.append((ps[-2] + ps[-1]) % m)
        return ps[:-1]
    
    def makeGrid(self, m, h):
        grid = VGroup(*[Tex(n) for n in self.pisanoSequence(m)])
        return grid.arrange_in_grid(rows=h, flow_order="dr")
    
    def makeGridLabel(self, m, h):
        label = MathTex("P(", m, ",", h, ")")
        label[1].set_color(RED)
        label[3].set_color(ORANGE)
        return label.scale(1.875).to_edge(UL)
    
    def palindromeAnim(self, mobjDict = {"mobj": VGroup()}):
        if type(mobjDict) == dict:
            mobjDict = [mobjDict]

        shiftAwayAnim = []
        for mobjItem in mobjDict:
            color = mobjItem.get("color", False)
            mobjItem["copy"] = mobjItem["mobj"].copy()
            anim = mobjItem["copy"].animate.shift(mobjItem.get("dir", DOWN))
            if color:
                anim.set_color(color)
            shiftAwayAnim += [anim]
            if mobjItem.get("sym", False):
                shiftAwayAnim += [mobjItem["mobj"].animate.shift(-mobjItem.get("dir", DOWN))]
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
            anim = mobjItem["copy"].animate.shift(-mobjItem.get("dir", DOWN))
            if mobjItem.get("color", False):
                anim.set_color(WHITE)
            shiftBackAnim += [anim]
            if mobjItem.get("sym", False): 
                shiftBackAnim += [mobjItem["mobj"].animate.shift(mobjItem.get("dir", DOWN))]
        self.play(*shiftBackAnim)

        for mobjItem in mobjDict:
            self.remove(mobjItem["copy"])