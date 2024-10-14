from manim import *
from templates import PisanoScene

class Outro(PisanoScene):
  def construct(self):
    super().construct()

    title = Text("Summary", font_size=89).to_edge(UP)

    with self.voiceover("Now, let's take some time to talk about all of this"):
      self.play(Write(title))

    with self.voiceover(
      """I think there's two main questions you might be asking yourself:
      did we actually <bookmark mark='prove'/>prove anything, and does this actually <bookmark mark='matter'/>matter?"""
    ):
      qs = VGroup(Tex("Did we prove anything? ", "Yes!"), Tex("Does this matter? ", "Maybe?")).scale(1.5).arrange(DOWN, buff=1.5).center()
      self.wait_until_bookmark('prove')
      self.play(Write(qs[0][0]))
      self.wait_until_bookmark('matter')
      self.play(Write(qs[1][0]))

    with self.voiceover(
      """Well even though our 'proofs' were observational, and that may seem lazy, <bookmark mark='yes'/>these patterns do exist. 
      If you can define a pattern within one of these arrays, and simply observe they work for every position you could move that pattern to,
      you 'have' proved that pattern, whether you felt like you did math or not. """
    ):
      self.wait_until_bookmark("yes")
      self.play(Write(qs[0][1]))

    with self.voiceover(
      """As for whether it matters, all I can say is, I hope so."""
    ):
      self.play(Write(qs[1][1]))

    with self.voiceover(
      """One place I think it makes sense to look for hope is the <bookmark mark='pisano'/>Pisano Period,
      which is how long the Fibonacci numbers take to repeat when taken a certain modulus. 
      This is known for some numbers, and there's tricks for deriving it without having to check in some cases, 
      but there's no general formula for how long they take to repeat. For some moduli, the only way to find out is to check.
      I think it's likely that patterns in the arrays could shed light on the Pisano period, but it's hard to say."""
    ):
      self.wait_until_bookmark("pisano")
      self.play(Transform(qs[1][1], MathTex(r"\pi(m)=?").scale(1.5).next_to(qs[1][0], RIGHT)))

    with self.voiceover("That still leaves the question, does the Pisano Period matter? Does this eventually come back to something someone would use?"):
      self.play(Transform(qs[1][1], MathTex(r"(\pi(m)=?)?").scale(1.5).next_to(qs[1][0], RIGHT)))

    with self.voiceover(
      """As I've gotten older though, that question has become less and less relevant to me. 
      There's examples all over of things in math not being considered useful until we found out a place that they were. 
      Now I'm not saying that eventually these patterns will show up in <bookmark mark='string'/>string theory,
      but at this point it's a bit tough to be surprised when something shows up in string theory."""
    ):
      self.wait_until_bookmark("string")
      self.play(Transform(qs[1][1], Tex("String Theory?").scale(1.5).next_to(qs[1][0], RIGHT)))

    with self.voiceover(
      """But if instead we look at if anyone got any value from this, and we consider simple enjoyment something we value,
      then I <bookmark mark='know'/>know this was valuable to me, as I hope it was for you."""
    ):
      self.wait_until_bookmark('know')
      self.play(Transform(qs[1][1], Tex("Yes").scale(1.5).next_to(qs[1][0], RIGHT)))

    with self.voiceover("Thank you for sticking to the end, and I'm looking forward to making some new content for you very soon. "):
      self.play(Transform(title, Text("Thanks!", font_size=89)), FadeOut(qs))

    self.play(FadeOut(title))
    self.wait()
