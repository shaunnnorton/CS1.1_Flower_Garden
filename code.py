#pylint:disable=E1101
import turtle as jerry
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
        """initialize the class"""
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
        """Draws the Tree"""
        jerry.setheading(0)
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
          

Flower1 = Flower(-300,0,5,"purple",50,10)
Tree1 = Tree(300,0,100,"green",70,10,40)
Flower2 = Flower(-200,0,8,"pink",50,10)
Tree2 = Tree(200,0,150,"orange",30,10,40)
Flower3 = Flower(-100,0,11,"red",50,10)
Tree3 = Tree(100,0,300,"yellow",7,10,40)
Flower1.draw() 
Flower2.draw()  
Flower3.draw()  
Tree1.draw() 
Tree2.draw() 
Tree3.draw() 

#Test for get_turn_degrees()
assert Flower1.get_turn_degrees(4) == 90
assert Flower1.get_turn_degrees(6) == 60
assert Flower1.get_turn_degrees(360) == 1
assert Flower1.get_turn_degrees(5) == 72





jerry.mainloop() 
