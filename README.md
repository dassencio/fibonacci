![Functional tests](https://github.com/dassencio/fibonacci/workflows/Functional%20tests/badge.svg)
![Static code analysis](https://github.com/dassencio/fibonacci/workflows/Static%20code%20analysis/badge.svg)

# Description

`fibonacci` is a script (written in Python 3) which computes any element of the
Fibonacci sequence with arbitrary precision. It implements the algorithm
described [here](https://diego.assencio.com/?index=c772250d88e35665d3a793882a7b70e5).

# License

All code from this project is licensed under the GPLv3. See the
[`LICENSE`](https://github.com/dassencio/fibonacci/tree/master/LICENSE)
file for more information.

# Required modules

The `gmpy2` module is used. You can install it with the following command:

    pip3 install gmpy2

On Ubuntu/Debian, you may need to install additional system packages before you
can install `gmpy2`:

    sudo apt install libmpfr-dev libmpc-dev

# Usage instructions

To get the N-th element of the Fibonacci sequence (N must be a nonnegative
integer), run:

    ./fibonacci N

# Notes on performance

Python is capable of dealing with arbitrarily long integers by design, but GMPY
is used instead for that purpose since it performs significantly better (for
large values of N, using GMPY can reduce the execution time by orders of
magnitude).

# Contributors & contact information

Diego Assencio / diego@assencio.com
