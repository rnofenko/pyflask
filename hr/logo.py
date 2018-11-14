if __name__ == '__main__':
	n = 3
	#n = int(input())

	col_size = (n - 1) * 2 + 1
	size = 1
	for i in range(n):
		s = 'H' * size
		s = s.center(col_size, ' ')
		print(s)
		size += 2

	whole_size = n * 5 + n // 2 * 2
	hline = 'H' * n
	emptyline = ' ' * n
	normline = (hline + emptyline * 3 + hline).center(whole_size, ' ')
	fullline = (hline * 5).center(whole_size, ' ')

	for i in range(n + 1):
		print(normline)

	for i in range(n // 2 + 1):
		print(fullline)

	for i in range(n + 1):
		print(normline)

	for i in range(n):
		size -= 2
		s = 'H' * size
		s = s.center(col_size, ' ')
		print(s.rjust(whole_size, ' '))
		