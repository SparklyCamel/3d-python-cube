# Simple cube with half of a face shaded
# with "fake" lighting

# This was a nightmare and I hate python,
# despite being ok at coding in it it's bad because
# of it's rigid indentation
import turtle
from math import sin,cos

root = turtle.Screen()
root.setup(600,600)
root.tracer(0)

def rotate(x,y,r):
    s, c = cos(r), sin(r)
    return (x * c) - (y * s), (x * s) + (y * c)

def base(n):
    if n == 0:
        n = 1
    
    return n

def hex(n):
    return ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'][max(0, min(int(n), 15))]
 
class world:
    EDGES = [(0,1), (1,2), (2,3), (3,0),(4,5), (5,6), (6,7), (7,4),(0,4), (1,5), (2,6), (3,7)]
    VERTS = [[-1,-1,-1],[1,-1,-1], [1,1,-1], [-1,1,-1], [-1,-1,1], [1,-1,1], [1,1,1], [-1,1,1]]

    def __init__(self):
        self.rX = 0
        self.rY = 0
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.begin_fill(); self.t.width(4.74)

    def draw(self):
        for edge in self.EDGES:
            points = []
            
            for vert in edge:
                x,y,z = self.VERTS[vert]

                x,z = rotate(x, z, self.rY)
                y,z = rotate(y, z, self.rX)
                x,y = rotate(x, y, self.rY)
                
            
                z += 5
                if z != 0:
                    f = 400/(z)
               
                sX, sY = x*f,y*f
                points.append(sX)
                points.append(sY)
                self.t.fillcolor('#' + hex((sX + sY + (z * f))/20) + 'f01ff')
            self.t.goto(points[0], points[1]); self.t.goto(points[2], points[3])
        
        self.t.end_fill()  

world = world()
while True:
    world.t.clear()
    world.draw()
    world.rX = root.getcanvas().winfo_pointerx() / -400
    world.rY = root.getcanvas().winfo_pointery() / 400
    root.update()