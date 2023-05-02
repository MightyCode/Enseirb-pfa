from random import sample
import time
class FallingBlocks:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[(0,0,0,0)] * height for _ in range(width)]
        self.falling_blocks = []
        # for i in range(height):
        #     self.grid[0][i] = 1
        self.print_grid()
        print()


    def remaining_columns(self):
        indices = []
        for i, column in enumerate(self.grid):
            if len(list(filter(lambda x: x != (0,0,0,0), column))) < len(column):
                indices.append(i)
        return indices



    def next(self):
        new_falling_blocks = []
        for block in self.falling_blocks:
            x, y = block
            if y+1 >= self.height:
                continue
            if self.grid[x][y+1] == (0,0,0,0):
                self.grid[x][y+1] = self.grid[x][y]
                self.grid[x][y] = (0,0,0,0)

                new_falling_blocks.append((x, y+1))
        self.falling_blocks = new_falling_blocks

        new_col = sample(self.remaining_columns(), k=1)[0]
        self.grid[new_col][0] = (255, 0, 0, 0)
        self.falling_blocks.append((new_col, 0))
        return self.grid

    def print_grid(self):
        for col in self.grid:
            print([cell[0] for cell in col])




f = FallingBlocks(6, 9)
f.next()
f.print_grid()
print()
while True:
    f.next()
    f.print_grid()
    print()
    time.sleep(1)
print(f.falling_blocks)

