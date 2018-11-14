import cmath

if __name__ == '__main__':
	input_text = '1+2j'
	x, y = map(int, input_text.replace('j','').split('+'))

	c = complex(input_text)

	r = abs(c)
	print(r)

	p = cmath.phase(c)
	print(p)