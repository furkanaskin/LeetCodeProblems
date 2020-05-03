import datetime
import sys

from BColors import BColors


# https://leetcode.com/problems/word-search/description/
class WordSearchBubbleSort:

    def __init__(self, input):
        self.query = input

        if not self.query:
            sys.exit("Query can't be empty.")
        elif not len(self.query) in range(1, 1001):
            sys.exit("Query len must be 1 between 1000")
        else:
            print("Query is " + self.query)

    query = None
    chars = []
    lastIndex = int(0)
    found = ""
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['S', 'G', 'X', 'S'],
        ['S', 'B', 'X', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    def bubbleSort(self, unsortedList):
        for passnum in range(len(unsortedList) - 1, 0, -1):
            for i in range(passnum):
                if unsortedList[i] > unsortedList[i + 1]:
                    temp = unsortedList[i]
                    unsortedList[i] = unsortedList[i + 1]
                    unsortedList[i + 1] = temp
        return unsortedList

    def innerLoop(self, searchingChar):
        print("Searching:", self.chars)
        for innerIndex in range(self.lastIndex, len(self.chars)):
            if self.chars[innerIndex] == searchingChar:
                self.found += searchingChar
                self.lastIndex = innerIndex
                self.chars.pop(innerIndex)
                print("Found : ", self.found)
                return True

    def sortBoard(self):
        for i in range(0, len(self.board)):
            for y in self.board[i]:
                self.chars.append(y)

        self.bubbleSort(self.chars)

    def isExists(self):
        begin_time = datetime.datetime.now()
        listFromQuery = list(self.query.upper())
        self.bubbleSort(listFromQuery)
        self.sortBoard()

        for i in listFromQuery:  # For loop inside query
            if list(self.query.upper()).sort() == list(self.found).sort() and len(list(self.found)) == len(
                    list(self.query.upper())):
                return

            if self.innerLoop(i):  # For loop inside board
                continue

        # hour:minute:second:microsecond, execution time of function
        print(BColors.OKBLUE + "Execution time :", datetime.datetime.now() - begin_time, BColors.ENDC)
        return list(self.query.upper()).sort() == list(self.found).sort() and len(list(self.found)) == len(
            list(self.query.upper()))


if __name__ == '__main__':
    wordSearchBubbleSort = WordSearchBubbleSort("sBXxSAfb")

    if wordSearchBubbleSort.isExists():
        print(BColors.OKGREEN + "Query found." + BColors.ENDC)
    else:
        print(BColors.FAIL + "Query not found." + BColors.ENDC)
