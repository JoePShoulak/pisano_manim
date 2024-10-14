from manim import *
from templates import *

class Fibonacci(PisanoScene):
    def construct(self):
        super().construct()
        
        with self.voiceover(
            """So today we're going to talk about Pisano Arrays,
            but first we have to start with the Fibonacci numbers"""):
            # Title and definition of the Fibonacci numbers
            title = Text("Fibonacci Numbers", font_size=89).to_edge(UP)
            subtitle = MathTex(r"f_{0} = 0, \ f_{1} = 1, \ f_{n}=f_{n-1}+f_{n-2}", font_size=55)
            subtitle.to_edge(UP, buff=2)
            self.play(Write(title))
        
        with self.voiceover("The fibonacci numbers have a simple enough definition: To get the <bookmark mark='next'/>next one, you add the previous two"):
            self.wait_until_bookmark('next')
            self.play(Write(subtitle, run_time=4))

        # Drawing the Fibonacci equations
        self.next_section("NUMBERS")
        with self.voiceover(
            """We start with 0 and 1 for some rather philisophical reasons, and then continue finding sums. 
            We <bookmark mark='find'/>find another 1, a 2, 3, 5, 8, 13, 21, 34, and so on
        """):
            vals = [0,1,1]
            eqns = VGroup(MathTex(*r"{:.0f}  +  {:.0f}  =  {:.0f}".format(*vals).split("  ")))
            for i in range(7):
                vals.append(vals[1]+vals[2])
                vals.pop(0)
                eqn = MathTex(*r"{:.0f}  +  {:.0f}  =  {:.0f}".format(*vals).split("  "))
                eqn.next_to(eqns[-1],DOWN).shift((eqns[-1][3].get_bottom()[0]-eqn[1].get_top()[0])*RIGHT)
                eqns += eqn
            eqns.next_to(subtitle, DOWN)
            self.wait_until_bookmark('find')
            self.play(Write(eqns), run_time=10)
    
        with self.voiceover(
            """As much as I love the way these equations <bookmark mark='ARRANGE'/>arrange themselves, we still have some work to do with these numbers. So let's clean them up!"""
        ):
            # Reducing the equations to the right hand side
            self.play(*[eqn.animate.become(eqn[4]) for eqn in eqns])

            # Aligning everything in one row with the numbers and elipsis
            self.wait(3)
            eqns.insert(0, MathTex("1").next_to(eqns[0], LEFT))
            eqns.insert(0, MathTex("0").next_to(eqns[0], LEFT))
            eqns += MathTex(r"\ldots").next_to(eqns[-1], RIGHT)
            self.play(
                AnimationGroup(Write(eqns[0]), Write(eqns[1]), Write(eqns[-1])),
                AnimationGroup(eqns.animate.arrange(RIGHT).shift(UP), FadeOut(subtitle)),
                lag_ratio=0.5
            )

        self.next_section("MODULUS")
        with self.voiceover("""We're going to start by taking the Fibonacci numbers modulus, or, mod 10. 
                            Taking the mod of something just means dividing by a number, but looking at the remainder instead of the answer to the division.
                            Conveniently, when doing so with <bookmark mark='mod10'/>10, that just leaves the one's digit."""):
            # New definition at the top of the screen
            self.wait_until_bookmark('mod10')
            subtitle = Tex("A number ", "modulus 10", " is the one's digit", font_size=55).to_edge(UP, buff=2)
            subtitle.set_color_by_tex("modulus 10", RED)
            self.play(Write(subtitle))
            self.wait()

        # Create our modulus numbers
        with self.voiceover("This leaves us with 0, 1, 1, 2, 3, 5, 8, 3, 1, 4, and so on"):
            modEqns = VGroup(*[MathTex(int((eqn if len(eqn) == 1 else eqn[4]).get_tex_string()) % 10).next_to(eqn, DOWN, buff=2) for eqn in eqns[:-1]])
            modEqns += MathTex(r"\ldots").next_to(modEqns[-1], RIGHT).align_to(eqns[-1], RIGHT)

            # Make an arrow with a label to be clear what we're doing
            arrow = Arrow(start=UP, end=DOWN).next_to(modEqns[0], UP)
            arrowGroup = VGroup(arrow, MathTex(r"\bmod_{10}", color=RED).add_updater(lambda l : l.next_to(arrow, RIGHT)))

            # Animate the taking of the modulus
            self.play(Write(modEqns[0]), Write(arrowGroup))
            for eqn in modEqns[1:-1]:
                self.play(
                    AnimationGroup(Write(eqn)),
                    AnimationGroup(arrow.animate.next_to(eqn, UP), run_time=0.33),
                    lag_ratio=0.5
                )
            self.play(Write(modEqns[-1]), FadeOut(arrowGroup))

        # Fade out the old numbers and shift these up; left shift is to be centered way later on
        with self.voiceover("Now we're almost ready to talk about Pisano Arrays"):
            self.play(modEqns.animate.arrange(RIGHT).to_edge(UP, buff=3).shift(LEFT*0.12590103), FadeOut(eqns))
            self.wait()

            self.next_section("OUTRO")
            self.play(Transform(title, Text("Pisano Arrays", font_size=89).to_edge(UP)), FadeOut(subtitle))
            self.wait()

