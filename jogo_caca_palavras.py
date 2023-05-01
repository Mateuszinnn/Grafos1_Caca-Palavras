from tkinter import *
import random
from tkinter import messagebox
from typing import List

class Solution:

    def __init__(self):
        # making the possible moves in movers array
        self.mover = [
            [1, 0], [0, 1], [-1, 0], [0, -1],
            [1, 1], [-1, -1], [1, -1], [-1, 1]
        ]

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        rows = len(board)
        cols = len(board[0])

        # making board a global variable
        self.board = board

        for word in words:
            for i in range(rows):
                for j in range(cols):
                    if self.board[i][j] == word[0]:

                        # making a function findwords to
                        # find words along with their
                        # location which inputs the board
                        # and list of words
                        if self.dfs(i, j, word[1:], [[False] * cols for _ in range(rows)]):
                            result.append(f"{word}")

        return result
    