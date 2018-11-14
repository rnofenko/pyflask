def getLine(size, dots_count):
	return '---' * size + '.' + '|..' * dots_count

if __name__ == '__main__':
	inp = '7 21'.split(' ')
	n, m = map(int, inp)
	
	changer = 1
	half = n // 2
	part_size = half
	dots_count = 0
	for i in range(n):
		if part_size == 0:
			print('WELCOME'.center(m, '-'))
			changer = -1
			part_size = 1
			dots_count += changer
		else:
			l = getLine(part_size, dots_count)
			print(l + '|' + l[::-1])
			part_size -= changer
			dots_count += changer