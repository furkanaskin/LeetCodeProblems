import datetime
import sys

from BColors import BColors


# https://leetcode.com/problems/word-search/description/

class WordSearchDivideAndConquer:

    def __init__(self, input):
        self.query = input

        if not self.query:
            sys.exit("Query can't be empty.")
        elif not len(self.query) in range(1, 1001):
            sys.exit("Query len must be 1 between 1000")
        else:
            print("Query is " + self.query)
            self.listFromQuery = list(self.query.upper())

    query = None
    found = ""
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['S', 'G', 'X', 'S'],
        ['S', 'B', 'X', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    listFromQuery = []
    index = len(board)
    searchedIndexes = []

    def divideAndConquer(self, board, size):

        if size % 2 == 0 and self.searchedIndexes.__contains__(size) == False:
            self.index = int((self.index / 2))

            print("Searching :", board[self.index - 1])
            for i in self.listFromQuery.copy():  # For loop inside query
                if list(self.query.upper()).sort() == list(self.found).sort() and len(list(self.found)) == len(
                        list(self.query.upper())):
                    return

                if self.innerLoop(i, board[self.index - 1]):  # For loop inside board
                    self.listFromQuery.remove(i)
                    continue

            self.searchedIndexes.append(self.index - 1)
            self.divideAndConquer(board, self.index)

        elif size % 2 == 1 and self.searchedIndexes.__contains__(size) == False:
            self.index = int((self.index / 2))

            print("Searching :", board[self.index - 1])
            for i in self.listFromQuery.copy():  # For loop inside query
                if list(self.query.upper()).sort() == list(self.found).sort() and len(list(self.found)) == len(
                        list(self.query.upper())):
                    return

                if self.innerLoop(i, board[self.index - 1]):  # For loop inside board
                    self.listFromQuery.remove(i)
                    continue

            self.searchedIndexes.append(self.index - 1)
            self.divideAndConquer(board, self.index)
        else:
            self.index = self.index + 1
            if self.index >= len(board):
                return

            print("Searching :", board[self.index])
            for i in self.listFromQuery.copy():  # For loop inside query
                if list(self.query.upper()).sort() == list(self.found).sort() and len(list(self.found)) == len(
                        list(self.query.upper())):
                    return

                if self.innerLoop(i, board[self.index]):  # For loop inside board
                    self.listFromQuery.remove(i)
                    continue

            self.searchedIndexes.append(self.index)
            self.divideAndConquer(board, self.index)

    def innerLoop(self, char, board):
        if board.__contains__(char):
            board.remove(char)
            self.found += char
            print("Found : ", self.found)
            return True

    def isExists(self):
        begin_time = datetime.datetime.now()
        self.divideAndConquer(self.board, len(self.board))

        # hour:minute:second:microsecond, execution time of function
        print(BColors.OKBLUE + "Execution time :", datetime.datetime.now() - begin_time, BColors.ENDC)
        return list(self.query.upper()).sort() == list(self.found).sort() and len(list(self.found)) == len(
            list(self.query.upper()))


if __name__ == '__main__':
    wordSearchDivideAndConquer = WordSearchDivideAndConquer("sBXxSAb")
    if wordSearchDivideAndConquer.isExists():
        print(BColors.OKGREEN + "Query found." + BColors.ENDC)
    else:
        print(BColors.FAIL + "Query not found." + BColors.ENDC)
