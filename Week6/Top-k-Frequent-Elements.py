class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hm = {}
        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        heap = []

        for key in hm:
            heapq.heappush(heap, (-hm[key], key))

        res = []
        for _ in range(k):
            popped = heapq.heappop(heap)
            res.append(popped[1])

        return res
