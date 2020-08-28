#pylint:disable=E1101
import turtle as jerry


def draw_flower(x, y, num_petals, petal_size, color, petal_length):
    """This function draws a flower using turtle graphics"""

    jerry.goto(x, y)
    jerry.pencolor(color)
    jerry.pensize(petal_size)

    # draw petals
    for _ in range(num_petals):
        jerry.forward(petal_length)
        jerry.backward(petal_length)
        jerry.right(360/num_petals)

    # draw center
    jerry.pencolor("orange")
    jerry.dot(50)


#draw_flower(0, 0, 6, 40, "pink", 100)


class Flower:
    """A Class for flowers"""
    def __init__(self,x,y,num_petals,color,petal_length,petal_size):
        """Initializing the class"""
        self.x = x
        self.y = y
        self.num_petals = num_petals
        self.color = color
        self.petal_length = petal_length
        self.petal_size = petal_size
    
    def get_turn_degrees(self,num_petals):
        """Returns the degrees needed to turn for the number of petals"""
        return 360/num_petals

    def draw(self):
        """Draws the Flower using Turtle graphics"""
        jerry.penup()
        jerry.goto(self.x,self.y)
        jerry.pendown()
        jerry.pensize(self.petal_size)
        jerry.pencolor(self.color)

        for _ in range(self.num_petals):
            jerry.forward(self.petal_length)
            jerry.backward(self.petal_length)
            jerry.right(Flower.get_turn_degrees(self,self.num_petals))
        
        jerry.pencolor("orange")
        jerry.dot(self.petal_size*2)

class Tree:
    def __init__(self ,x,y,height,color,num_leaves,leaf_size,leaf_length,trunk_color="brown"):
        self.x = x
        self.y = y
        self.height = height
        self.color = color 
        self.num_leaves = num_leaves
        self.trunk_color = trunk_color
        self.leaf_size = leaf_size
        self.leaf_length = leaf_length
     
    def get_turn_degrees(self,num_leaves):
        """Returns the degrees needed to turn for the number of leaves"""
        return 360/num_leaves
    
    def draw(self):
        jerry.penup()
        jerry.goto(self.x,self.y)
        jerry.pendown()
        jerry.pensize(self.leaf_size)
        jerry.pencolor(self.trunk_color)
        jerry.right(90)
        jerry.forward(self.height)
        jerry.backward(self.height)
        jerry.pencolor(self.color)
        jerry.right(Tree.get_turn_degrees(self,self.num_leaves))

        for _ in range(self.num_leaves):
            jerry.forward(self.leaf_length)
            jerry.backward(self.leaf_length)
            jerry.right(Tree.get_turn_degrees(self,self.num_leaves))

          

Flower1 = Flower(-50,0,8,"purple",50,10)
assert Flower1.get_turn_degrees(4)==90 , "get_turn_degrees returned the wrong value"
Flower1.draw()
Tree1 = Tree(50,0,90,"green",70,10,40)
Tree1.draw()



jerry.mainloop() 