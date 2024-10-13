from manim import *
from templates import *

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
