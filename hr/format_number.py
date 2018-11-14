if __name__ == '__main__':
	n = 17
	l = len('{0:b}'.format(n))
	templates = [ '{0}', '{0:o}','{0:x}' ]
	for i in range(1,n+1):
		for t in templates:			
			print(t.format(i).upper().rjust(l) + ' ', end='')
		print('{0:b}'.format(i).rjust(l))