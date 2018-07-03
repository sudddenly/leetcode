# Runtime: 76ms

class Solution(object):
	def flipAndInvertImage(self, A):
		"""
		:type A: List[List[int]]
		:rtype: List[List[int]]
		"""
		if len(A) == 0:
			return A
		res = []
		for row in A:
			res.append([])  # 每行先加一个空list
			for col in row[::-1]:
				tmp = 1 - col # 实现很简单
				res[-1].append(tmp)
		return res