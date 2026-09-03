from manim import *

class Linklist(Scene):
    def construct(self):

        #create node
        node1 = VGroup(
            Square(side_length=1),
            Text("10")
        )
        node2 = VGroup(
            Square(side_length=1),
            Text("20")
        )
        node3 = VGroup(
            Square(side_length=1),
            Text("30")
        )
        node4 = VGroup(
            Square(side_length=1),
            Text("40")
        )
        node5 = VGroup(
            Square(side_length=1),
            Text("Null", font_size=20)
        )
        node6 = VGroup(
            Square(side_length=1),
            Text("Null", font_size=20)
        )


        #arrage nodes horizontally
        nodes = VGroup(node6,node1,node2,node3,node4,node5)
        nodes.arrange(RIGHT, buff=1) ##buff is gap


        #create arrow
        arrow1 = Arrow(
            node1.get_right(),
            node2.get_left(),
            buff=0.1
        )

        arrow2 = Arrow(
            node2.get_right(),
            node3.get_left(),
            buff=0.1
        )

        arrow3 = Arrow(
            node3.get_right(),
            node4.get_left(),
            buff=0.1
        )
        arrow4 = Arrow(
            node4.get_right(),
            node5.get_left(),
            buff=0.1
        )
        arrownull = Arrow(
            node1.get_left(),
            node6.get_right(),
            buff= 0.1
        )


        arrowrev3 = Arrow(
            node4.get_left(),
            node3.get_right(),
            buff=0.1
        )
        arrowrev2 =Arrow(
            node3.get_left(),
            node2.get_right(),
            buff=0.1
        )
        arrowrev1 = Arrow(
            node2.get_left(),
            node1.get_right(),
            buff=0.1
        )
        

        arrow3.shift(UP * 0.1)
        arrowrev3.shift(DOWN *0.1)

        arrow2.shift(UP * 0.1)
        arrowrev2.shift(DOWN * 0.1)

        arrow1.shift(UP *0.1)
        arrowrev1.shift(DOWN *0.1)


        #create text
        text = Text("Double Link List")
        text.to_edge(DOWN)

        #animate text
        self.play(Write(text))

        #animate nodes and arrow

        self.play(Create(node1))
        self.play(Create(arrow1))

        self.play(Create(node2))
        self.play(Create(arrow2))
        
        self.play(Create(node3))
        self.play(Create(arrow3))

        self.play(Create(node4))
        self.play(Create(arrow4))

        self.play(Create(node5))

        self.play(Create(arrowrev3))
        self.play(Create(arrowrev2))
        self.play(Create(arrowrev1))

        self.play(Create(node6))
        self.play(Create(arrownull))


        

        self.wait(2)

