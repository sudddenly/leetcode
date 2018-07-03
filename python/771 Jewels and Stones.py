class Solution(object):
	def numJewelsInStones(self, J, S):
		"""
		:type J: str
		:type S: str
		:rtype: int
		:Runtime: 40ms
		"""

		return sum([s in J for s in S])
