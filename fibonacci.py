#!/usr/bin/python3


import sys
import os
from gmpy2 import mpz


def mult_2x2(A,B):
	"""
	Computes the matrix product C = A*B and returns the result as a tuple
	(c11, c12, c21, c22). Both A and B must be 2x2 matrices stored as
	4-tuples in the form (a11, a12, a21, a22) and (b11, b12, b21, b22)
	respectively.
	"""

	return (A[0]*B[0] + A[1]*B[2],    # a11*b11 + a12*b21
	         A[0]*B[1] + A[1]*B[3],    # a11*b12 + a12*b22
	         A[2]*B[0] + A[3]*B[2],    # a21*b11 + a22*b21
	         A[2]*B[1] + A[3]*B[3])    # a21*b12 + a22*b22


def pow_2x2(M,n):
	"""
	Computes R = M^n, where M is a 2x2 matrix stored as a 4-tuple in the
	form (m11, m12, m21, m22) and n is a nonnegative integer. The result
	is returned as a 4-tuple (r11, r12, r21, r22).

	This function uses exponentiation by squaring to compute M^n.
        """

	if n < 0:
		raise ValueError

	# for n = 0, return the identity matrix
	if n == 0:
		return (1,0,0,1)

	if n % 2 == 0:
		return pow_2x2(mult_2x2(M,M), n/2)
	else:
		return mult_2x2(M, pow_2x2(mult_2x2(M,M), (n-1)/2))


def fibonacci(n):
	"""
	Computes the n-th element of the Fibonacci sequence with arbitrary
	precision, where n is a nonnegative integer.
	"""

	if n < 0:
		raise ValueError

	M = (mpz(1), mpz(1),
	     mpz(1), mpz(0))

	return pow_2x2(M,n)[2]

def main():
	if len(sys.argv) < 2:
		sys.stderr.write("usage: %s INTEGER\n" % os.path.basename(__file__))
		sys.exit(1)

	try:
		print(fibonacci(mpz(sys.argv[1])))
	except:
		sys.stderr.write("error: invalid input integer (must be nonnegative)\n")
		sys.exit(1)


if __name__ == '__main__':
	main()
