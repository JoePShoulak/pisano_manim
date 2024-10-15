from manim import *
from templates import PisanoScene

def mySquare(size):
  return Square(side_length=size).set_fill(YELLOW, opacity=.7).flip(LEFT)

def myArc(size):
  return Arc(angle=PI/2, radius=size).flip(LEFT).rotate(-PI/2)

class Intro(PisanoScene, MovingCameraScene):
  def construct(self):
    super().construct()
    with self.voiceover("intro"):
      pass

    scaleFactor = 2

    playTime = 0.5

    sq1 = mySquare(1/scaleFactor)
    self.play(Create(sq1), run_time=playTime) # Create current square
    self.play(sq1.animate.set_stroke(RED), run_time=playTime) # Set current square stroke red

    arc1 = myArc(1/scaleFactor).align_to(sq1, DL)
    sq2 = mySquare(1/scaleFactor).next_to(sq1, UP, buff=0).rotate(-0*PI/2).align_to(sq1, LEFT)
    self.play(
      Create(sq2), # Create current square
      sq1.animate.set_fill(ORANGE, opacity=.7), # Set old square to orange
      self.camera.frame.animate.shift(UP*1/2/scaleFactor), run_time=playTime
    )
    self.play(
      Create(arc1), # Create arc in old square
      sq2.animate.set_stroke(RED), run_time=playTime # Set current square stroke red
    )

    arc2 = myArc(1/scaleFactor).rotate(-1*PI/2).align_to(sq2, DL)
    sq3 = mySquare(2/scaleFactor).next_to(sq2, RIGHT, buff=0).rotate(-1*PI/2).align_to(sq2, UP)
    self.play(
      Create(sq3), # Create current square
      sq2.animate.set_fill(ORANGE, opacity=.7), # Set old square to orange
      self.camera.frame.animate.shift(RIGHT*2/2/scaleFactor), run_time=playTime
    )
    self.play(
      Create(arc2), # Create arc in old square
      sq3.animate.set_stroke(RED), run_time=playTime # Set current square stroke red
    )

    arc3 = myArc(2/scaleFactor).rotate(-2*PI/2).align_to(sq3, DL)
    sq4 = mySquare(3/scaleFactor).next_to(sq3, DOWN, buff=0).rotate(-2*PI/2).align_to(sq3, RIGHT)
    self.play(
      Create(sq4), # Create current square
      sq3.animate.set_fill(ORANGE, opacity=.7), # Set old square to orange
      self.camera.frame.animate.shift(DOWN*3/2/scaleFactor), run_time=playTime
    )
    self.play(
      Create(arc3), # Create arc in old square
      sq4.animate.set_stroke(RED), run_time=playTime # Set current square stroke red
    )

    arc4 = myArc(3/scaleFactor).rotate(-3*PI/2).align_to(sq4, DL)
    sq5 = mySquare(5/scaleFactor).next_to(sq4, LEFT, buff=0).rotate(-3*PI/2).align_to(sq4, DOWN)
    self.play(
      Create(sq5), # Create current square
      sq4.animate.set_fill(ORANGE, opacity=.7), # Set old square to orange
      self.camera.frame.animate.shift(LEFT*5/2/scaleFactor), run_time=playTime
    )
    self.play(
      Create(arc4), # Create arc in old square
      sq5.animate.set_stroke(RED), run_time=playTime # Set current square stroke red
    )

    arc5 = myArc(5/scaleFactor).rotate(-4*PI/2).align_to(sq5, DL)
    sq6 = mySquare(8/scaleFactor).next_to(sq5, UP, buff=0).rotate(-4*PI/2).align_to(sq5, LEFT)
    self.play(
      Create(sq6), # Create current square
      sq5.animate.set_fill(ORANGE, opacity=.7), # Set old square to orange
      self.camera.frame.animate.shift(UP*8/2/scaleFactor), run_time=playTime
    )
    self.play(
      Create(arc5), # Create arc in old square
      sq6.animate.set_stroke(RED), run_time=playTime # Set current square stroke red
    )

    arc6 = myArc(8/scaleFactor).rotate(-5*PI/2).align_to(sq6, DL)
    sq7 = mySquare(13/scaleFactor).next_to(sq6, RIGHT, buff=0).rotate(-5*PI/2).align_to(sq6, UP)
    self.play(
      Create(sq7), # Create current square
      sq6.animate.set_fill(ORANGE, opacity=.7), # Set old square to orange
      self.camera.frame.animate.shift(RIGHT*13/2/scaleFactor), run_time=playTime
    )
    self.play(
      Create(arc6), # Create arc in old square
      sq7.animate.set_stroke(RED), run_time=playTime # Set current square stroke red
    )

    arc7 = myArc(13/scaleFactor).rotate(-6*PI/2).align_to(sq7, DL)
    self.play(sq7.animate.set_fill(ORANGE, opacity=.7), run_time=playTime)
    self.play(Create(arc7), run_time=playTime)

    self.wait()
    self.play(
      FadeOut(*[i for i in [sq1, sq2, sq3, sq4, sq5, sq6, sq7]]),
      FadeOut(*[i for i in [arc1, arc2, arc3, arc4, arc5, arc6, arc7]]),
    )
    self.wait()
