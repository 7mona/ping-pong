import turtle

class Paddle(turtle.Turtle):
    
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.create(x_cor,y_cor)
        
    def create(self,x_cor,y_cor):
        
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(x_cor,y_cor)
        
    
    def go_up(self):
        self.goto(self.xcor(),self.ycor()+20)
        
    def go_down(self):
        self.goto(self.xcor(),self.ycor()-20)