from manim import *
from templates import TenFivePattern

class TenFiveLucas(TenFivePattern):
    def construct(self):
        super().construct()
        self.writeSummary(Tex("All rows but the top arethe same but ", "shifted", font_size=55).set_color_by_tex("shifted", self.HIGHLIGHT))

        # Prep the grid for manipulation
        rows = VGroup(*[VGroup(*[self.grid[i] for i in range(j,60+j, 5)]) for j in range(5)])
        self.play(self.grid.animate.center().shift(DOWN))
        self.wait()

        self.play(FadeOut(rows[0]), self.highlight(rows[1:]))
        self.wait()

        gridWidth = rows[1][1].get_bottom()[0] - rows[1][0].get_bottom()[0]
        # Extend the rows
        for row in rows[1:]:
            for i in range(10):
                b, c = int(row[0].get_tex_string()), int(row[1].get_tex_string())
                row.insert(0, Tex((c - b) % 10).scale(1.25).move_to(row[0].get_center()).shift(LEFT*gridWidth))
            for i in range(10):
                a, b = int(row[-2].get_tex_string()), int(row[-1].get_tex_string())
                row.add(Tex((a+b) % 10).scale(1.25).move_to(row[-1].get_center()).shift(RIGHT*gridWidth))
        newNumsAnim = []
        for row in rows[1:]:
            for i in [*range(0, 10), *range(22, 32)]: 
                newNumsAnim += [Write(row[i])]
        self.play(*newNumsAnim)
        self.wait()

        # Align the rows
        self.play(
            rows[2].animate.align_to(rows[1][27], RIGHT),
            rows[3].animate.align_to(rows[1][26], RIGHT),
            rows[4].animate.align_to(rows[1][28], RIGHT)
        )
        self.wait(1.5)
        self.play(
            rows[4].animate.align_to(rows[1], UP).set_color(WHITE),
            rows[3].animate.align_to(rows[1], UP).set_color(WHITE),
            rows[2].animate.align_to(rows[1], UP).set_color(WHITE),
            rows[1].animate.set_color(WHITE)
        )
        self.wait(3)

        # Cleanup
        self.play(Transform(rows, self.makeGrid()), FadeOut(self.summary))
        self.wait()
     