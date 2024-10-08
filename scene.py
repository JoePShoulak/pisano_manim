from manim import *

class Fibonacci(Scene):
    def construct(self):
        # Title and definition of the Fibonacci numbers
        title = Text("Fibonacci Numbers", font_size=89).to_edge(UP)
        fibDef = MathTex(r"f_{0} = 0, \ f_{1} = 1, \ f_{n}=f_{n-1}+f_{n-2}", font_size=55).next_to(title, DOWN)
        self.wait()
        self.play(Write(title))
        self.play(Write(fibDef))

        # Drawing the fibonacci equations
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
        eqns.next_to(fibDef, DOWN)
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
            AnimationGroup(eqns.animate.arrange(RIGHT).shift(UP), FadeOut(fibDef)),
            lag_ratio=0.5
        )
        self.wait(1)

        modDef = Tex("A number modulus 10 is the one's digit", font_size=55).next_to(title, DOWN)
        self.play(Write(modDef))
        self.wait(1)

        modBuff = 2.0
        modEqns = VGroup(
            *[MathTex(int(eqn.get_tex_string()) % 10).next_to(eqn, DOWN, buff=modBuff) for eqn in eqns[:2]],
            *[MathTex(int(eqn[4].get_tex_string()) % 10).next_to(eqn, DOWN, buff=modBuff) for eqn in eqns[2:-1]]
        )
        modEqns += MathTex(r"\ldots").next_to(modEqns[-1], RIGHT).align_to(eqns[-1], RIGHT)

        aro = Arrow(start=UP, end=DOWN).next_to(modEqns[0], UP)
        modArrow = VGroup(aro, MathTex(r"\bmod 10").next_to(aro, RIGHT))

        self.play(Write(modArrow))
        self.play(Write(modEqns))
        self.wait(1)

class Pisano(Scene):
    def construct(self):
        title = Text("Pisano Arrays", font_size=89).shift(UP * 3)
        self.add(title)

        nums = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]

# class Test(Scene):
#     def construct(self):
#         vals = [0,1,1]
#         eqns = VGroup(
#             MathTex(*r"{:.0f}  +  {:.0f}  =  {:.0f}".format(*vals).split("  "))
#         )
#         for i in range(6):
#             vals.append(vals[1]+vals[2])
#             vals.pop(0)
#             eqn = MathTex(*r"{:.0f}  +  {:.0f}  =  {:.0f}".format(*vals).split("  "))
#             eqn.next_to(eqns[-1],DOWN).shift((eqns[-1][3].get_bottom()[0]-eqn[1].get_top()[0])*RIGHT)
#             eqns += eqn
#         eqns.center()
#         self.play(Write(eqns))
#         self.wait(1)
        
#         for eqn in eqns:
#             self.play(Transform(eqn, eqn[4]))
#         self.wait(1)

#         self.play(eqns.animate.arrange(RIGHT))
