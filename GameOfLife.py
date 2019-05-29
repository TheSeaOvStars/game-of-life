import random

class GameOfLife:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.grid = [[random.getrandbits(1) for i in range(y)] \
        for j in range(x)]



    def countNeighbours(self, x, y):
        neighbours = 0
        if (x > 0):
            neighbours = neighbours + self.grid[x-1][y]
        if (y > 0):
            neighbours = neighbours + self.grid[x][y-1]
        if (x > 0) and (y > 0):
            neighbours = neighbours + self.grid[x-1][y-1]
        if (x < self.x - 1):
            neighbours = neighbours + self.grid[x+1][y]
        if (y < self.y - 1):
            neighbours = neighbours + self.grid[x][y+1]
        if (y < self.y - 1) and (x < self.x - 1):
            neighbours = neighbours + self.grid[x+1][y+1]
        if (y < self.y - 1) and (x > 0):
            neighbours = neighbours + self.grid[x-1][y+1]
        if (x < self.x - 1) and (y > 0):
            neighbours = neighbours + self.grid[x+1][y-1]
        return neighbours



    def step(self):
        TempGrid = [row[:] for row in self.grid]
        for x in range(self.x):
            for y in range(self.y):
                Neighbours = self.countNeighbours(x,y)
                if self.grid[x][y] == 1:
                    if (Neighbours < 2) or (Neighbours > 3):
                        TempGrid[x][y] = 0
                elif Neighbours == 3:
                    TempGrid[x][y] = 1
        self.grid = [row[:] for row in TempGrid]
        return TempGrid