[![Build Status](https://travis-ci.org/dassencio/fibonacci.svg?branch=master)](https://travis-ci.org/dassencio/fibonacci/)

Description
===========

`fibonacci` is a small python script which computes any element of the
Fibonacci sequence with arbitrary precision.


License
=======

All code from this project is licensed under the GPLv3. See `LICENSE` for more.


Instructions
============

On Linux, just run `./fibonacci N` to get the N-th element of the Fibonacci
sequence (N must be a nonnegative integer).


Required Libraries
==================

The `gmpy2` library is used. On Ubuntu/Debian, you can install it with:

	sudo apt-get install python3-gmpy2


Notes on Performance
====================

Python is capable of dealing with arbitrarily long integers by design, but GMPY
is used instead for that purpose since it performs significantly better (for
large values of N, using GMPY can reduce the execution time by orders of
magnitude).


Contributors & Contact Information
==================================

Diego Assencio / diego@assencio.com
