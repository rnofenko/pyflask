from functools import reduce

if __name__ == '__main__':
	input_str = '161 182 161 154 176 170 167 171 170 174'
	input_str = '1 2 3 3 3 3'
	print(input_str)
	
	a = input_str.split(' ')
	print(a)

	a = map(int, a)

	s = set(a)
	print(s)

	r = reduce(lambda x, y: x + y, s)
	print(r)