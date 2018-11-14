def getLeftLine(i, n, chars):
	s = ''
	for j in range(i + 1, n):
		s += '-' + chars[j]
	return s

def getFull(i, n, chars):
	line = getLeftLine(i, n, chars) 
	full = line[::-1] + chars[i] + line
	return full.center((n - 1) * 4 + 1, '-')

if __name__ == '__main__':
	n = 5

	chars = list()
	for i in range(0,n):
		chars.append(chr(97 + i))
	
	for i in range(n - 1, -1, -1):
		print(getFull(i, n, chars))
	
	for i in range(1, n):
		print(getFull(i, n, chars))