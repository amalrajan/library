import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass



def compute_lps(pattern, m):
	lps = [0] * m
	length = 0

	i = 1
	while i < m:
		if pattern[i] == pattern[length]:
			length += 1
			lps[i] = length
			i += 1
		elif length != 0:
			length = lps[length - 1]
		else:
			lps[i] = 0
			i += 1

	return lps


def KMP(pattern, text):
	m, n = len(pattern), len(text)
	lps = compute_lps(pattern, m)

	j = 0
	i = 0
	while i < n:
		if pattern[j] == text[i]:
			i += 1
			j += 1

		if j == m:
			print('Found pattern at {}'.format(i - j))
			j = lps[j - 1]
		elif i < n and pattern[j] != text[i]:
			if j != 0:
				j = lps[j - 1]
			else:
				i += 1


text = 'ABABDABACDABABCABAB'
pattern = 'ABABCABAB'

KMP(pattern, text)
