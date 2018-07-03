# runtime 37ms
class Solution(object):
	def uniqueMorseRepresentations(self, words):
		"""
		:type words: List[str]
		:rtype: int
		"""

		d = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
		     "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
		trans = lambda x: d[ord(x) - ord('a')]
		map_word = lambda word: ''.join([trans(x) for x in word])
		res = map(map_word, words)
		return len(set(res))
