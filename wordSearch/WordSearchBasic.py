import datetime
import sys

from BColors import BColors


# https://leetcode.com/problems/word-search/description/

class WordSearchBasic:

    def __init__(self, input):
        self.query = input

        if not self.query:
            sys.exit("Query can't be empty.")
        elif 1 > len(self.query) > 1000:
            sys.exit("Query len must be 1 between 1000")
        else:
            print("Query is " + self.query)

    query = None
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['S', 'G', 'X', 'S'],
        ['S', 'B', 'X', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    def innerLoop(self, char):
        if 200 < len(self.board) < 1:
            return False

        for y in self.board:
            print("Searching:", y)
            for x in y:
                if 200 < len(self.board) < 1:
                    return False

                if char == x:
                    y.remove(x)
                    return True

    def isExists(self):
        begin_time = datetime.datetime.now()
        listFromQuery = list(self.query.upper())
        found = ""

        for i in listFromQuery:  # For loop inside query
            if self.query.upper() == found:
                return

            if self.innerLoop(i):  # For loop inside board
                found += i
                continue

        # hour:minute:second:microsecond, execution time of function
        print(BColors.OKBLUE + "Execution time :", datetime.datetime.now() - begin_time, BColors.ENDC)
        return self.query.upper() == found


if __name__ == '__main__':
    wordSearchBasic = WordSearchBasic("sBXxSAb")
    if wordSearchBasic.isExists():
        print(BColors.OKGREEN + "Query found." + BColors.ENDC)
    else:
        print(BColors.FAIL + "Query not found." + BColors.ENDC)
