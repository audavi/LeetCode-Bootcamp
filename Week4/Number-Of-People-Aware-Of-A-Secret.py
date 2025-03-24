class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        fq, dq, sharing = [0] * forget, [0] * delay, 0
        fq[0], dq[0] = 1, 1
        for i in range(n - 1):
            sharing += dq.pop(-1) - fq.pop(-1)
            new = sharing
            dq = [new] + dq
            fq = [new] + fq

        return sum(fq) % 1000000007