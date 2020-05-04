import sys


# https://leetcode.com/problems/daily-temperatures/description/

class DailyTemperatures:
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    remainingDays = []

    def __init__(self):
        if not len(self.temperatures) in range(1, 30001):
            sys.exit("Temperatures len must be in 1..30000")

    def calculateWarmerDays(self):
        for i in range(0, len(self.temperatures)):
            if not self.temperatures[i] in range(30, 100):
                sys.exit("Temperatures must be in 30..100")
            elif not self.findWarmer(i):
                self.remainingDays.append(0)
        print(self.remainingDays)

    def findWarmer(self, position):
        for j in range(position + 1, len(self.temperatures)):
            if self.temperatures[j] > self.temperatures[position]:
                self.remainingDays.append(j - position)
                return True
        return False


if __name__ == '__main__':
    dailyTemperatures = DailyTemperatures()
    dailyTemperatures.calculateWarmerDays()
