from manim import *

def mySquare(size):
  return Square(side_length=size).set_fill(YELLOW, opacity=.7).flip(LEFT)

def myArc(size):
  return Arc(angle=PI/2, radius=size).flip(LEFT).rotate(-PI/2)

class Intro(Scene):
  def construct(self):
    sq1 = mySquare(1)
    self.play(Create(sq1)) # Make current square
    self.play(sq1.animate.set_stroke(RED)) # Set current square stroke red

    arc1 = myArc(1).align_to(sq1, DL)
    sq2 = mySquare(1).next_to(sq1, UP, buff=0).rotate(0*-PI/2).align_to(sq1, LEFT)
    self.play(
      Create(sq2), # Make current square
      sq1.animate.set_fill(ORANGE, opacity=.7), # Set old square to orange
      sq2.animate.set_stroke(RED), # Set current quare stroke red
      Create(arc1) # Create arc in old square
    )

    # and so on

    # arc2 = myArc(1).rotate(-1*PI/2).align_to(sq2, DL)
    # sq3 = mySquare(2).next_to(sq2, RIGHT, buff=0).rotate(1*-PI/2).align_to(sq2, UP)
    # self.play(Create(sq3), sq2.animate.set_fill(ORANGE, opacity=.7))
    # self.play(sq3.animate.set_stroke(RED), Create(arc2))

    # arc3 = myArc(2).rotate(-2*PI/2).align_to(sq3, DL)
    # sq4 = mySquare(3).next_to(sq3, DOWN, buff=0).rotate(-2*PI/2).align_to(sq3, RIGHT)
    # self.play(Create(sq4), sq3.animate.set_fill(ORANGE, opacity=.7))
    # self.play(sq4.animate.set_stroke(RED), Create(arc3))

    # arc4 = myArc(3).rotate(-3*PI/2).align_to(sq4, DL)
    # sq5 = mySquare(5).next_to(sq4, LEFT, buff=0).rotate(-3*PI/2).align_to(sq4, DOWN)
    # self.play(Create(sq5), sq4.animate.set_fill(ORANGE, opacity=.7))
    # self.play(sq5.animate.set_stroke(RED), Create(arc4))

    # arc5 = myArc(5).rotate(-4*PI/2).align_to(sq5, DL)
    # self.play(sq5.animate.set_fill(ORANGE, opacity=.7))
    # self.play(Create(arc5))

    # self.wait()
