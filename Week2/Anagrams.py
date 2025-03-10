class Solution(object):
    def findAnagrams(self, s, p):
        n = len(s)
        m = len(p)

        p = Counter(p)
        answer = []
        window = None

        for i in range(0, n - m + 1):
            if i == 0:
                window = Counter(s[:m])
            else:
                window[s[i - 1]] -= 1
                window[s[i + m - 1]] += 1
            if len(window - p) == 0:
                answer.append(i)

        return answer
