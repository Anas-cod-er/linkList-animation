from manim import *

class Linklist(Scene):
    def construct(self):

        #create node
        node1 = VGroup(
            Square(side_length=1),
            Text("1")
        )
        node2 = VGroup(
            Square(side_length=1),
            Text("2")
        )
        node3 = VGroup(
            Square(side_length=1),
            Text("3")
        )
        node4 = VGroup(
            Square(side_length=1),
            Text("4")
        )
        node5 = VGroup(
            Square(side_length=1),
            Text("5")
        )


        #arrage nodes horizontally
        nodes = VGroup(node1,node2,node3,node4,node5)
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

        #animate nodes

        self.play(Create(node1))
        self.play(Create(node2))
        self.play(Create(node3))
        self.play(Create(node4))
        self.play(Create(node5))

        #animate arrows
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.play(Create(arrow3))
        self.play(Create(arrow4))

        self.wait(2)

