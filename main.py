from manim import *

# not pretty code, but it is functional!

class SequenceOfFunctions(Scene):
    def construct(self):
        axes = Axes(
            x_range = [-4,4,1], 
            y_range=[-2,2,1],
            tips = False
            )
        self.add(axes)

        text = MathTex(
            "f_n(x) = \Bigg\{", font_size=36
        ).to_corner(UL)
        text2 = MathTex(
            "nx", font_size=36
        ).next_to(text, RIGHT)
        text1 = MathTex(
            "1", font_size=36
        ).next_to(text2, UP, buff=0.3)
        text3 = MathTex(
            "-1", font_size=36
        ).next_to(text2, DOWN, buff=0.3)
        
        range2 = Tex(
            "$-\\frac{1}{n} \leq x \leq \\frac{1}{n}$ ", font_size=21
        ).next_to(text2, RIGHT, buff = 0.5)
        range1 = Tex(
            "$\\frac{1}{n}< x$", font_size=21
        ).next_to(range2, UP)
        range3 = Tex(
            "$x<-\\frac{1}{n}$", font_size=21
        ).next_to(range2, DOWN)
        
        self.add(text, text1, range1, text2, range2, text3, range3)
        self.wait()

        f1_n = axes.plot(lambda x: -1, x_range = [-3, -1], color=PINK)
        f2_n = axes.plot(lambda x: x, x_range = [-1, 1], color=PINK)
        f3_n = axes.plot(lambda x: 1, x_range = [1, 3], color=PINK)
        f_label = axes.get_graph_label(f2_n, label=r"f_1", color=PINK)
        self.play(Write(f1_n))
        self.play(Write(f2_n))
        self.play(Write(f3_n))
        self.play(Write(f_label))
        #self.play(FadeIn(f1_n, f2_n, f3_n, f_label))
        
        for n in range(2,10):
            self.play(FadeOut(f2_n, f_label))
            f1_n = axes.plot(lambda x: -1, x_range = [-3, -1/n], color=PINK)
            f2_n = axes.plot(lambda x: n*x, x_range = [-1/n, 1/n], color=PINK)
            f3_n = axes.plot(lambda x: 1, x_range = [1/n, 3], color=PINK)
            f_label = axes.get_graph_label(f2_n, label="f_%d" % n, color=PINK)
            self.play(FadeIn(f1_n, f2_n, f3_n, f_label))
        
        self.play(FadeOut(f_label))
        f_label = axes.get_graph_label(f2_n, label="...", color=PINK)
        self.play(Write(f_label))
        self.wait()
        self.play(FadeOut(f1_n, f2_n, f3_n, f_label))

        f1_n = axes.plot(lambda x: -1, x_range = [-3, 0], color=PINK)
        f2_n = Dot(radius=0.08,color=PINK)
        f3_n = axes.plot(lambda x: 1, x_range = [0, 3], color=PINK)
        self.play(FadeIn(f1_n, f2_n, f3_n))
        self.play(Write(Tex("!!!").next_to(f2_n, DR)))

            
        
        