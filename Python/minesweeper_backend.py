from typing import List
from collections import deque

DIRECTIONS = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

class Minesweeper:

    def __init__(self, m, n, mine_locs: List[List[int]]):
        self.board = [[-1] * n for _ in range(m)]
        for x, y in mine_locs:
            self.board[x][y] = 9

    def click(self, x, y) -> int:

        # check if they clicked a mine
        if self.board[x][y] == 9:
            return -1

        q = deque([(x, y)])
        while q:
            x, y = q.pop()
            self.board[x][y] = self.count_adj_mines(x, y)
            # only search neighbors if there are no adj mines
            if self.board[x][y] != 0:
                continue
            
            # search unrevealed neighbors
            for dx, dy in DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                # bounds check
                if new_x < 0 or new_x >= len(self.board) or new_y < 0 or new_y >= len(self.board[0]):
                    continue
                
                if self.board[new_x][new_y] != -1:
                    continue

                # search in-bounds, unrevealed neighbors
                q.appendleft((new_x, new_y))

        return 0

    def count_adj_mines(self, x, y) -> int:
        count = 0
        for dx, dy in DIRECTIONS:
            # bounds check
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_x >= len(self.board) or new_y < 0 or new_y >= len(self.board[0]):
                continue

            if self.board[new_x][new_y] != 9:
                continue

            count += 1
        
        return count

    def __str__(self) -> str:
        str_board = ""
        for row in self.board:
            str_board += str(row) + "\n"

        return str_board


if __name__ == "__main__":

    m, n = 5, 5
    mine_locs = [[1, 2], [3, 1]]
    game = Minesweeper(m, n, mine_locs)
    result = game.click(4, 0)
    print(result)
    result = game.click(0, 4)
    print(result)
    print(game)
