from manim import *
from templates import TenFivePattern

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
            r"&= 5k\\",
            r"f_{10}&=55=5k_2\\",
            r"f_5&=5=5k_1", font_size=34,
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
                r"&= 55f_{15n-9} + 34f_{15n-10}\\",
                r"&= 89f_{15n-10} + 55f_{15n-11}\\",
                font_size=34,
            ), MathTex(
                r"&= 144f_{15n-11} + 89f_{15n-12}\\",
                r"&= 233f_{15n-12} + 144f_{15n-13}\\",
                r"&= 377f_{15n-13} + 233f_{15n-14}\\",
                r"&= 610f_{15n-14} + 377f_{15n-15}\\",
                r"&= 610f_{15n-14} + 377f_{15(n-1)}\\",
                r"&= 610f_{15n-14} + 377 \times 10m\\",
                r"&= 10(61f_{15n-14} + 377m)\\",
                r"&= 10k \\",
                r"f_{30}&=832,040=10k_2\\",
                r"f_{15}&=610=10k_1", font_size=34,
            )
        ).arrange(RIGHT, buff=2).next_to(reminder, DOWN)

        for line in proof:
            self.play(Write(line))

        self.wait(3)
        self.play(FadeOut(proof), FadeOut(self.title), FadeOut(reminder))
        self.wait()
