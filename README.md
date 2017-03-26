[![Build Status](https://travis-ci.org/dassencio/fibonacci.svg?branch=master)](https://travis-ci.org/dassencio/fibonacci/)

Description
===========

`fibonacci` is a script (written in Python 3) which computes any element of the
Fibonacci sequence with arbitrary precision. It implements the algorithm
described [here](https://diego.assencio.com/?index=c772250d88e35665d3a793882a7b70e5).


License
=======

All code from this project is licensed under the GPLv3. See the `LICENSE` file
for more information.


Required modules
================

The `gmpy2` module is used. On Ubuntu/Debian, you can install it with the
following command:

	sudo apt-get install python3-gmpy2


Usage instructions
==================

To get the N-th element of the Fibonacci sequence (N must be a nonnegative
integer), run:

	./fibonacci N


Notes on performance
====================

Python is capable of dealing with arbitrarily long integers by design, but GMPY
is used instead for that purpose since it performs significantly better (for
large values of N, using GMPY can reduce the execution time by orders of
magnitude).


Contributors & contact information
==================================

Diego Assencio / diego@assencio.com
