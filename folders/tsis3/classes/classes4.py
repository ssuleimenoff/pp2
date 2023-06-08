class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x += x
        self.y += y
        return self.x, self.y

    def dist(self, pntx, pnty):
        self.pntx = pntx
        self.pnty = pnty
        dx = pntx - self.x
        dy = pnty - self.y
        return dx, dy


s1 = int(input())
s2 = int(input())
point = point(s1, s2)
print(point.show())
print(point.move(int(input()), int(input())))
print(point.dist(int(input()), int(input())))
