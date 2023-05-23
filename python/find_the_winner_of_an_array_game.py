class Solution(object):
    def getWinner(self, arr, k):
        wins = 0
        num = arr[0]
        it = 0

        while wins < k:
            if num > arr[1]:
                wins += 1
                loser = arr.pop(1)
                arr.append(loser)
            else:
                wins = 1
                loser = arr.pop(0)
                arr.append(loser)
                num = arr[0]
            it += 1
            # optimize for large k
            if (it) >= len(arr):
                return num
        return num
