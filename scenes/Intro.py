from manim import *

def mySquare(size):
  return Square(side_length=size).set_fill(YELLOW, opacity=.7).flip(LEFT)

def myArc(size):
  return Arc(angle=PI/2, radius=size).flip(LEFT).rotate(-PI/2)

class Intro(MovingCameraScene):
  def construct(self):
    def fibonacciTilingAnimation(oldSq, oldArc, newSq):
      self.play(
        Create(newSq), # Create current square
        oldSq.animate.set_fill(ORANGE, opacity=.7), # Set old square to orange
      )
      self.play(
        Create(oldArc), # Create arc in old square
        newSq.animate.set_stroke(RED) # Set current square stroke red
      )

    allSquares = VGroup()
    self.camera.frame.add_updater(lambda fr: fr.move_to(allSquares.get_center()))

    scaleFactor = 2

    sq1 = mySquare(1/scaleFactor)
    allSquares += sq1
    self.play(Create(sq1)) # Create current square
    self.play(sq1.animate.set_stroke(RED)) # Set current square stroke red

    arc1 = myArc(1/scaleFactor).align_to(sq1, DL)
    sq2 = mySquare(1/scaleFactor).next_to(sq1, UP, buff=0).rotate(-0*PI/2).align_to(sq1, LEFT)
    allSquares += sq2
    fibonacciTilingAnimation(sq1, arc1, sq2)

    arc2 = myArc(1/scaleFactor).rotate(-1*PI/2).align_to(sq2, DL)
    sq3 = mySquare(2/scaleFactor).next_to(sq2, RIGHT, buff=0).rotate(-1*PI/2).align_to(sq2, UP)
    allSquares += sq3
    fibonacciTilingAnimation(sq2, arc2, sq3)

    arc3 = myArc(2/scaleFactor).rotate(-2*PI/2).align_to(sq3, DL)
    sq4 = mySquare(3/scaleFactor).next_to(sq3, DOWN, buff=0).rotate(-2*PI/2).align_to(sq3, RIGHT)
    allSquares += sq4
    fibonacciTilingAnimation(sq3, arc3, sq4)

    arc4 = myArc(3/scaleFactor).rotate(-3*PI/2).align_to(sq4, DL)
    sq5 = mySquare(5/scaleFactor).next_to(sq4, LEFT, buff=0).rotate(-3*PI/2).align_to(sq4, DOWN)
    allSquares += sq5
    fibonacciTilingAnimation(sq4, arc4, sq5)

    arc5 = myArc(5/scaleFactor).rotate(-4*PI/2).align_to(sq5, DL)
    sq6 = mySquare(8/scaleFactor).next_to(sq5, UP, buff=0).rotate(-4*PI/2).align_to(sq5, LEFT)
    allSquares += sq6
    fibonacciTilingAnimation(sq5, arc5, sq6)

    arc6 = myArc(8/scaleFactor).rotate(-5*PI/2).align_to(sq6, DL)
    sq7 = mySquare(13/scaleFactor).next_to(sq6, RIGHT, buff=0).rotate(-5*PI/2).align_to(sq6, UP)
    allSquares += sq7
    fibonacciTilingAnimation(sq6, arc6, sq7)

    arc7 = myArc(13/scaleFactor).rotate(-6*PI/2).align_to(sq7, DL)
    self.play(sq7.animate.set_fill(ORANGE, opacity=.7))
    self.play(Create(arc7))

    self.wait()
