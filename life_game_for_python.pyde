import math
class Gen:
    def __init__(self):
        # self.cells = [
        #     0,0,0,0,0,0,0,0,
        #     0,0,0,1,0,0,0,0,
        #     0,1,0,1,0,0,0,0,
        #     0,0,1,1,0,0,0,0,
        #     0,0,0,0,0,0,0,0,
        #     0,0,0,0,0,0,0,0,
        #     0,0,0,0,0,0,0,0,
        #     0,0,0,0,0,0,0,0,
        # ]
        self.cells = [
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,1,1,0,1,1,1,1,1,1,0,0,0,
            0,0,0,0,1,1,0,1,1,1,1,1,1,0,0,0,
            0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,
            0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,
            0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,
            0,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,
            0,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
        ]
        return
    def next(self):
        t = self
        n = Gen()
        # n.cells = [1] * len(self.cells)
        for i in range(len(t.cells)):
            x,y = t.index_to_xy(i)
            alive_num = t.livesAround(x,y)
            if t.cells[i] == 0:
                # 現世代で死んでているセルは…
                # ３個の生きているセルに囲まれてたら復活
                n.cells[i] = 1 if alive_num == 3 else 0
            else:
                # 現世代で生きているセルは…
                # ２個か３個の生きているセルに囲まれてれば生存，それ以外なら過疎か過密で死
                n.cells[i] = 1 if alive_num == 2 or alive_num == 3 else 0
        return n
    
    def livesAround(self,x,y):
        alive_num = 0
        for i in range(-1,2):
            for j in range(-1,2):
                # print("(i,j)=({0},{1}) x+i={2}, y+i={3}".format(i,j,x+i,y+j))
                index = self.xy_to_index(x+i,y+j)
                # print("index: {0}".format(index))
                alive_num += 0 if index == -1 else self.cells[int(index)]
        alive_num -= self.cells[int(self.xy_to_index(x,y))]
        return alive_num
    
    def xy_to_index(self,x,y):
        # print("x={0},y={1}".format(x,y))
        w = math.sqrt(len(self.cells))
        if x<0 or x>=w or y<0 or y>=w:
            return -1
        return y*w + x
    
    def index_to_xy(self,i):
        w = math.sqrt(len(self.cells))
        x = i % w
        y = math.floor(i/w)
        return x,y
    
    def draw(self):
        fill(0, 51, 153)
        stroke(255,255,255)
        for i,c in zip(range(len(self.cells)),self.cells):
            x,y = self.index_to_xy(i)
            w = height/math.sqrt(len(self.cells))
            # print("x={0},y={1},w={2}".format(x,y,w))
            if( c == 1):
                rect(w*x, w*y, w, w)
        return

g = Gen()

def redrawAll():
    background(204,204,255)
    g.draw()
    # print(g.cells)
    return

def setup():
    global g
    size(480,480)
    redrawAll()
    return

def mousePressed():
    global g
    g = g.next()
    redrawAll()
    return

def draw():
    if frameCount%10 == 9:
        mousePressed()
    return
    
