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
    
    # depth first search for the string, with the
    # coordinates and a visited array to take care that we
    # do not overlap the places visited already
    def dfs(self, x: int, y: int, s: str, vis: List[List[bool]]) -> bool:

        # if string length becomes 0 means string is found
        if not s:
            return True

        vis[x][y] = True

        # making a solution boolean to see if we can
        # perform depth search to find answer
        sol = False

        # making possible moves
        for move in self.mover:
            currX = move[0] + x
            currY = move[1] + y

            # checking for out of bound areas
            if 0 <= currX < len(self.board) and 0 <= currY < len(self.board[0]):

                # checking for similarity in the first
                # letter and the visited array
                if self.board[currX][currY] == s[0] and not vis[currX][currY]:
                    if self.dfs(currX, currY, s[1:], vis):
                        # removing the first letter
                        # from the string
                        sol = True

        return sol