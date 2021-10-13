#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc
import matplotlib.pyplot as plt

def fib_py(n):
	if n  <= 1:
		return n
	else:
		return (fib_py(n-1)+fib_py(n-2))

def main():
	print('Running on python code:')
	xs = list(range(30,46))
	ys_py = []
	ys_c = []
#	for n in xs:
#		start = pc()
#		k = fib_py(n)
#		end = pc()
#		ys_py.append(end-start)
#		print(f'Calculated {n}th fib in {round(end-start,2)} seconds, {k}')
	ys_py = [0.46,0.74,1.2,1.94,3.14,5.08,8.19,13.26,21.5,34.71,56.2,91.06,147.47,238.52,385.95,624.08]

	print('Running on C++ code:')
	for n in xs:
		start = pc()
		f = Integer(n)
		fb = f.fib()
		end = pc()
		ys_c.append(end-start)
		print(f'Calculated {n}th fib in {round(end-start,2)} seconds, {fb}')
	plt.plot(xs, ys_py)
	plt.plot(xs, ys_c)
	plt.savefig('fib.png')

if __name__ == '__main__':
	main()
