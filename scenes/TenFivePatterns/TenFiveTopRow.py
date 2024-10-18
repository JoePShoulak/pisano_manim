from manim import *
from templates import TenFivePattern

class TenFiveTopRow(TenFivePattern):
    def construct(self):
        super().construct()
        with self.voiceover("Now, you may be wondering why I left this pattern so late, since you maybe noticed it first."):
            self.writeSummary(Tex("The top row is all ", "5", "s and ", "0", "s", font_size=55).set_color_by_tex("5", self.HIGHLIGHT).set_color_by_tex("0", self.HIGHLIGHT))
            self.play(self.highlight(VGroup(*[self.grid[i] for i in range(0, 60, 5)])))
            self.wait(0.5)
        
        with self.voiceover(
            """The reason is, this one isn't too bad to prove algebraically.
            So for those unsatisfied with a purely observational proof, we can do some actual math now.
        """):
            self.play(self.unhighlight(self.grid))
            gridFrame = VGroup(self.summary, self.grid, self.label)
            self.play(FadeOut(gridFrame), Transform(self.title, Tex("Proof: $f_{5n}=5k$", font_size=89).to_edge(UP)))
            self.wait()

        with self.voiceover(
            """So we're trying to prove every fifth Fibonacci number is a multiple of 5.
            I'll show you how to do that using nothing but the <bookmark mark='def'/>definition of the Fibonacci numbers,
            and something called inductive reasoning.
        """):
            reminder = MathTex(r"f_{n}=f_{n-1}+f_{n-2}", font_size=55).next_to(self.title, DOWN)
            self.wait_until_bookmark('def')
            self.play(Write(reminder))

        vos = [
            "We start by decomposing f sub 5 n into the two numbers that came before it",
            "Then we do that same thing, but to the largest Fibonacci number on the right side.",
            "and do it again",
        ]

        # Proof that F(5n) = 5k
        proof = MathTex(
            r"f_{5n} &= f_{5n-1} + f_{5n-2}\\",
            r"&= 2f_{5n-2} + f_{5n-3}\\",
            r"&= 3f_{5n-3} + 2f_{5n-4}\\",
            r"&= 5f_{5n-4} + ", r"3f_{5n-5}\\",
            r"&= 5f_{5n-4} + ", r"3f_{5(n-1)}\\",
            r"&= 5f_{5n-4} + ", r"3 \times 5m\\",
            r"&= 5(f_{5n-4} + 3m)\\",
            r"f_{5n} &= 5k\\",
            r"f_{10}&=55=5k_2\\",
            r"f_5&=5=5k_1", font_size=34,
        ).next_to(reminder, DOWN)

        for vo, line in zip(vos, proof):
            with self.voiceover(vo):
                self.play(Write(line))

        with self.voiceover(
            """and after one more time you may begin noticing these terms have Fibonacci numbers in them! That's no coincidence, and helps make this work. 
            <bookmark mark='so'/>So now we have 5 times some Fibonacci number, plus 3 times another Fibonacci number, f sub 5 n minus 5"""):
            self.play(Write(proof[3:5]))
            self.wait_until_bookmark('so')
            self.play(proof[4].animate.set_color(self.HIGHLIGHT))

        with self.voiceover("but we could rewrite that same number <bookmark mark='as'/>as f sub 5 times n minus one"):
            self.play(Write(proof[5:7]), proof[3:5].animate.set_color(WHITE))
            self.wait_until_bookmark('as')
            self.play(proof[6].animate.set_color(self.HIGHLIGHT))

        with self.voiceover("which, if our hypothesis is correct, <bookmark mark='is'/>is itself a multiple of 5"):
            self.play(Write(proof[7:9]), proof[5:7].animate.set_color(WHITE))
            self.wait_until_bookmark('is')
            self.play(proof[8].animate.set_color(self.HIGHLIGHT))

        with self.voiceover("that means we can factor a 5 out of our entire definition of f sub 5 n"):
            self.play(Write(proof[9]), proof[7:9].animate.set_color(WHITE))

        with self.voiceover("""and since all that's left is an integer, we're safe replacing it with k, therefore proving our point. Well, almost.
            At this point, we've basically proven that if some Fibonacci number with an index that's a multiple of 5 is itself a multiple of 5,
            then that would be true for the Fibonacci number 5 terms after it, and 5 terms after that, and so on. We still need to prove there's some situation where it's true at all.
            As my Discrete Mathematics teacher taught me, induction is like climbing a ladder. First you prove that the ladder 'works', then you find the bottom few rungs to prove it 'exists'."""):
            self.play(Write(proof[10]))

        with self.voiceover(
            """So, by writing the first two Fibonacci numbers that meat our pattern (above zero), we can think about 'climbing up' this proof. 
            We start with the two things that are obviously true, and continue climbing up the logic until we reach our general proof. 
            Beautiful, isn't it? """
        ):
            self.play(Write(proof[-2:]))

        with self.voiceover(
            """For those that were craving this level of algebra all-video-long, here's a homework problem for you:
            <bookmark mark='prove'/>Prove that every 15th Fibonacci number is a multiple of 10, which would explain the 0s in our grid."""
        ):
            self.wait_until_bookmark("prove")
            self.play(Transform(proof, Tex("?").scale(3)), FadeOut(reminder), Transform(self.title, Tex("Proof: $f_{15n}=10k$", font_size=89).to_edge(UP)))

        with self.voiceover(
            """As a disclaimer, this isn't the most rigorous example of proof by induction,
            but I hope that it gave you a feel of what we're trying to do, and how we're trying to do it."""):
            self.play(FadeOut(proof), FadeOut(self.title))
