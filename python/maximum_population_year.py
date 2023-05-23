class Solution(object):
    def maximumPopulation(self, logs):
        born = {}
        died = {}
        for pair in logs:
            b = pair[0]
            d = pair[1]
            if born.get(b):
                born[b] += 1
            else:
                born[b] = 1
            if died.get(d):
                died[d] += 1
            else:
                died[d] = 1

        min_year = min([year for year in born])
        max_year = max([year for year in died])

        people = 0
        max_people = 0
        ans = None
        for y in range(min_year, max_year + 1):
            if born.get(y):
                people += born[y]
            if died.get(y):
                people -= died[y]
            if people > max_people:
                max_people = people
                ans = y
        return ans
