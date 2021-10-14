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
	for n in xs:
		start = pc()
		k = fib_py(n)
		end = pc()
		ys_py.append(end-start)
		print(f'Calculated {n}th fib in {round(end-start,2)} seconds, {k}')

	print('Running on C++ code:')
	for n in xs:
                start = pc()
                f = Integer(n)
		fb = f.fib()
		end = pc()
		ys_c.append(end-start)
		print(f'Calculated {n}th fib in {round(end-start,2)} seconds, {fb}')
        with open('data.txt', 'w') as f:
                for x in xs[:-1]:
                        f.write(str(x) + ',')
                f.write('\n')
                for x in ys_py[:-1]:
                        f.write(str(x) + ',')
                f.write('\n')
                for x in ys_c[:-1]:
                        f.write(str(x) + ',')
        
	plt.plot(xs, ys_py)
	plt.plot(xs, ys_c)
	plt.savefig('fib.png')

if __name__ == '__main__':
	main()
