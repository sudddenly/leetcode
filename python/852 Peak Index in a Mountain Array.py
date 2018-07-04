# Runtime 119ms
class Solution(object):
	def peakIndexInMountainArray(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		low = 0
		high = len(A) - 1
		while low < high:
			middle = (low + high) // 2
			if A[middle] < A[middle + 1]:
				low = middle +1
			else:
				high = middle
		return low

"""
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
#:type A: List[int]
#:rtype: int
#Runtime: 56 ms
"""
return A.index(max(A))
"""
