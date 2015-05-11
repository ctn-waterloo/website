title: Neural Engineering book

Two members of the CNRG, [Chris Eliasmith](/people/chris-eliasmith.html)
and Charles H. Anderson,
wrote a book detailing the framework presented here. The
title is *"Neural Engineering: Computation, Representation and Dynamics
in Neurobiological Systems."*
The official MIT Press website is
[here](http://mitpress.mit.edu/books/neural-engineering).
The book is also available at
[Amazon](http://www.amazon.com/exec/obidos/ASIN/0262050714/dictionaofphilosA/102-7106411-9852917).

Please send us an [email](mailto:celiasmith@uwaterloo.ca) if you have
any questions or have found errors in the book (see errata below).

## Errata

### Major

1. Figure 4.21 (p. 121) is printed incorrectly.
   The bottom response traces are missing. It should look like
   [this](http://compneuro.uwaterloo.ca/files/erratafigure4.21.gif).
2. Section 2.2.1 reports real neuron information transmission rates as about
   $3^{10}$ bits/s. This should be between about 10-700 bit/s
   (depending on the neuron).
3. In Appendix B, equation B.17, the convolution ($*$) is a multiplication.
   This is because the equation expresses the convolution explicitly
   (once you remove the $*$).
4. Figure 4.3 should have values of $\alpha=1.7$, $J^{bias}=1.0 nA$,
   and $J_{th}=0.1 nA$ (values in the book were missing the decimal place).
   In addition, 4.3c is incorrect. It is approximately correct
   to reverse the order of the legend labels.

### Minor

1. Appendix B, p. 309: the first sentence after equation B.21 should read
   "where $\langle \rangle_A$ is the convolution with the
   window to emphasize that this *is* providing an approximation..."
   The word 'is' is missing.
2. There's an errant bracket in the subscript for equation B.6.
3. Appendix B: B.6 should be $x(t;A)$, not $x(t;p)$.
   B.11 Should have a factor of $2 \pi$ in front.
   B.12 Should have no factors in front.
   B.16 $t \alpha$ should be $t^\alpha$, the brackets should be squared,
   $(t-t^\alpha)^2$, and the expression should be normalized,
   i.e., multiplied by $1 / \Delta_t \sqrt(2 \pi)$.
4. In chapter 9, eqns 9.9 and 9.10 should have $p(y|x)$ in place of $p(x|y)$
   (p. 278).
