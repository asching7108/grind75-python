class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        total = 0
        for task in tasks:
            count[ord(task) - ord('A')] += 1
            total += 1

        ans = 0
        while total:
            count.sort(reverse=True)
            for i in range(n + 1):
                if i < 26 and count[i] > 0:
                    count[i] -= 1
                    total -= 1
                ans += 1
                if total == 0:
                    break

        return ans
