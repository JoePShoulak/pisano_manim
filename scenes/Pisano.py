from manim import *
from templates import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

def pisanoSequence(m):
    ps = [0, 1]
    while ps[-2:] != [1, 0]:
        ps.append((ps[-2] + ps[-1]) % m)
    return ps[:-1]

class Pisano(VoiceoverScene):
    def construct(self):
        self.set_speech_service(AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",))
        
        # Recreate everything from the last scene
        with self.voiceover(
            """The Fibonacci numbers mod 10 repeat every 60.
            This is called the Pisano Period.
            In fact, the Fibonacci numbers mod anything will repeat eventually,
            but we'll focus on 10 for now"""
        ):
            pisanoTitle = Text("Pisano Arrays", font_size=89).to_edge(UP)
            subtitle = MathTex(r"\text{The Fibonacci numbers} \bmod_", "{10}", r" \text{ repeat every 60, so } \pi(", "10", ")=60", font_size=34)
            subtitle.to_edge(UP, buff=2).set_color_by_tex("10", RED)
            modEqns = VGroup(*[MathTex(n) for n in [*pisanoSequence(10)[:10], r"\ldots"]])
            modEqns.arrange(RIGHT).to_edge(UP, buff=3).shift(LEFT*0.12590103)
            self.add(pisanoTitle)
            self.add(modEqns)
            self.play(Write(subtitle))

        self.next_section("PISANO SEQUENCE 10")
        with self.voiceover(
            """So lets add the rest of the Fibonaccis mod 10 so we can begin to look for patterns"""
        ):
        # Remove the dots
            dots = modEqns[-1]
            modEqns.remove(dots)

            # Write in the rest of the numbers
            for num in pisanoSequence(10)[10:]:
                modEqns.add(MathTex(num).next_to(modEqns[-1], RIGHT))
            self.play(FadeOut(dots), Write(modEqns[10:]))
            self.wait()
            
            # Fade out the pisano period mention
            self.play(FadeOut(subtitle))
            self.wait()

        self.next_section("P(10,5) DEFINITION")
        with self.voiceover(
            """They're not too easy to analyze running off screen like that, so let's arrange them into a grid.
               We already chose a modulus of 10, so once we choose a height, say, 5, we're all set!
            """):
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

        with self.voiceover(
            """This is a Pisano Array, and is defined like so, with a modulus and a height.
            """):
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
        with self.voiceover(
            """
                Now we can get to the actually fun part: pattern hunting.
                So put on your best archaeologist hat (never leave it behind), and follow me!
            """):
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
