import time
import random
from typing import List, Tuple, Generator


class Life:
    state: List[List[bool]]
    m: int
    n: int

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.state = [[False for _ in range(n)] for _ in range(m)]

    def __repr__(self) -> str:
        return str(self.state)

    def random_select(self, rate):
        for x_grid in range(self.m):
            for y_grid in range(self.n):
                if random.randint(0, rate) == 0:
                    self.state[x_grid][y_grid] = True

    def neighbours(self, i: int, j: int) -> Generator[Tuple[int, int], None, None]:
        for x_grid in range(-1, 2):
            for y_grid in range(-1, 2):
                if self.m > i + x_grid >= 0 and self.n > j + y_grid >= 0 \
                        and not (x_grid == y_grid == 0):
                       yield i + x_grid, j + y_grid

    def nextstate(self) -> None:
        next_ = self.state.copy()

        for x_grid in range(self.m):
            for y_grid in range(self.n):
                num_of_on = 0
                for cell in self.neighbours(x_grid, y_grid):

                    try:
                        if self.state[cell[0]][cell[1]]:
                            num_of_on += 1
                    except:
                        print(x_grid, y_grid)
                        print(cell[0], cell[1])
                        return

                if self.state[x_grid][y_grid]:
                    if num_of_on not in (2, 3):
                        next_[x_grid][y_grid] = False
                elif num_of_on == 3:
                    next_[x_grid][y_grid] = True

        self.state = next_

    def addfigure(self, i: int, j: int, figure: List[str]) -> None:
        if i + len(figure) > self.m:
            raise ValueError

        for x_grid in range(len(figure)):
            if len(figure[x_grid]) > self.n - j:
                raise ValueError

            for y_grid in range(len(figure[x_grid])):
                self.state[x_grid + i][y_grid + j] = figure[x_grid][y_grid] not in ". "

    def __str__(self) -> str:
        grid = ""
        for x_grid in range(self.m):
            for y_grid in range(self.n):
                if self.state[x_grid][y_grid]:
                    grid += '# '
                else:
                    grid += '. '

            grid += '\n'
        return grid
