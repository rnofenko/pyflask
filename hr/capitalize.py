if __name__ == '__main__':
	s = "chris alan"
	a = s.split(' ')
	r = ''
	for p in a:
		r += ' ' + p.capitalize()

	print(r[1:])
    