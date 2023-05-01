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
    
def cria_jogo(palavras: List[str], tamanho_grade: int) -> List[List[str]]:
        # Criar uma matriz quadrada de tamanho 'tamanho_grade' por 'tamanho_grade' com letras aleatórias
        grade = [[random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(tamanho_grade)] for _ in
                range(tamanho_grade)]

        # Colocar as palavras na matriz
        for palavra in palavras:
            direcoes = ['horizontal', 'vertical', 'diagonal']
            direcao = random.choice(direcoes)
            linha = random.randint(0, tamanho_grade - 1)
            coluna = random.randint(0, tamanho_grade - 1)

            # Verificar se é possível colocar a palavra na direção escolhida
            palavra_valida = False
            if direcao == 'horizontal':
                if coluna + len(palavra) <= tamanho_grade:
                    palavra_valida = True
            elif direcao == 'vertical':
                if linha + len(palavra) <= tamanho_grade:
                    palavra_valida = True
            elif direcao == 'diagonal':
                if linha + len(palavra) <= tamanho_grade and coluna + len(palavra) <= tamanho_grade:
                    palavra_valida = True

            # Colocar a palavra na matriz
            if palavra_valida:
                for i in range(len(palavra)):
                    if direcao == 'horizontal':
                        grade[linha][coluna + i] = palavra[i]
                    elif direcao == 'vertical':
                        grade[linha + i][coluna] = palavra[i]
                    elif direcao == 'diagonal':
                        grade[linha + i][coluna + i] = palavra[i]

        return grade

def gera_jogo():
    global size
    words = palavra_entry.get().lower().split(",")
    size = int(tamanho_entry.get())
    game = cria_jogo(words, size)
    # Text box
    resposta_text = Text(height=size, width=2*size)
    resposta_text.grid(row=3, column=0, columnspan=3)
    resposta_text.config(state="disabled")
    resposta_text.config(state="normal") 
    resposta_text.delete("1.0", 'end')
    resposta_text.insert('end', game)
    resposta_text.config(state="disabled")

    window.mainloop()

if __name__ == '__main__':
    window = Tk()
    window.title("Caça-Palavras")
    window.config(padx=10, pady=10)

    # Labels
    palavra_label = Label(text="Palavras (separadas por vírgula):")
    palavra_label.grid(row=0, column=0)

    tamanho_label = Label(text="Tamanho da grade:")
    tamanho_label.grid(row=1, column=0)

    resposta_label = Label(text="Jogo:")
    resposta_label.grid(row=2, column=0)

    # Entries
    palavra_entry = Entry(width=35)
    palavra_entry.grid(row=0, column=1, columnspan=2)
    palavra_entry.focus()

    tamanho_entry = Entry(width=35)
    tamanho_entry.grid(row=1, column=1, columnspan=2)

    # Text box
    resposta_text = Text(height=20, width=50)
    resposta_text.grid(row=3, column=0, columnspan=3)
    resposta_text.config(state="disabled")

    # Button
    add_button = Button(text="Gerar Jogo", width=36, command=gera_jogo)
    add_button.grid(row=4, column=1, columnspan=2)

    window.mainloop()