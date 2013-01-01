Bessel functions in Scipy
=========================

:date: 2012-12-03
:tags: programmation, maths
:summary: Untangling the special functions

Bessel functions of the first kind, :math:`J_l` where :math:`l` is an integer,
are found in ``scipy.special.jn``. This is a function that takes two arguments:
the first one is the value of :math:`l` and the second one is the value of the
point at which to evaluate the functions. If one is interested in :math:`J_0`
or :math:`J_1` only, then there are faster implementations of these functions
as ``j0`` and ``j1``.

If the goal is to find the zeros of the Bessel function, then rather than using
a root finding routine (such as ``scipy.optimize.newton``) it is more efficient
to call ``scipy.special.jn_zeros``. This function also takes two arguments, the
first one is the value of :math:`l` and the second one is the number of zeros
to display (it starts at the first positive zero).

For Bessel functions of half-integer order, so called *spherical Bessel
function*, the situation is a little bit more complicated. The appropriate
function is ``scipy.special.sph_jn``. To compute :math:`J_{l + 1/2}`, the first
argument to ``sph_jn`` is the value of :math:`l`. The second argument is the
value of the point at which to evaluate the function. Where it gets complicated
is in the return value of the function. ``sph_jn`` returns a pair of arrays.
The first array contains the values of the function, and the second array
contains the values of the derivative.  Each array has length :math:`l + 1` and
contains a value for all spherical Bessel functions with :math:`l` smaller than
or equal to the supplied value.

It is useful to wrap this function into something friendlier:

.. code:: python

    def j3o2(x):
        """Compute the spherical Bessel function J_{3/2}."""
        return sph_jn(1, x)[0][1]

    def j5o2(x):
        """Compute the spherical Bessel function J_{5/2}."""
        return sph_jn(2, x)[0][2]

To obtain the zeros of the spherical Bessel function, one has to call a root
finding procedure. For instance, ``scipy.optimize.newton`` does the job quite
well.

John D. Cook has a `great page`_ about Bessel functions and `another one`_
about how to work with the implementation in Scipy.

.. _`great page`: http://www.johndcook.com/Bessel_functions.html
.. _`another one`: http://www.johndcook.com/Bessel_python.html

