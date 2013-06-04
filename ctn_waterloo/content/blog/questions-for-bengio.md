title: Questions for Bengio
author: Charlie Tang
date: 2012-01-28 17:32

  1. Does a feed forward step for projecting an out of sample onto a learned manifold exist and what is the accuracy to the closest location on the manifold to the out of sample   

  2. Why hasn't feature selection received much attention in deep networks, i think it's important for example, trying to (or during learning) pick out objects of interest with background clutter   

  3. Given the observation he made that RBM's energy fn is bilinear, and the question he made regarding the possibility of increase the capacity of RBM without adding #, but rather use nonparametric formulation; with nonparametric formulation of energy, the first thing i think of are mixture modeling or dirichlet process type of stuff; how to deal with learning, and what about the curse of dim (in specifying the nonparametric parameters), and how does this relate to the fact that RBM are "combinatorial machines" borrowing the term from Freund. And does nonparametric formulation means that the energy will be a local representation?   

  4. What did he exactly mean when he say "P(X) and P(Y|X) are unrelated as a function of X", i can see that with MNIST data, P(X) is high when P(Y=y|X) is high at some region of X. is this what he means? Furthermore, is it possible to use a more formal measurement, and say, a distribution is cooperative if the mutual information I(y,h) is high when we unsupervised-ly learn h using only X ? would this mean that I(y,x) must be really really high? what about this idea of using max mutual information as a criterion to learning layer by layer?   

  5. What's the role of the fact that in a DBN, the approximate P(H|X) is given by W'x plays role in helping either optimization or regularization when training a deep discriminative network?   

  6. Doesn't Lee et al's sparse RBM idea violate the combinatorial machine construction for RBMs?   

  7. How well does random firing in RBMs reflect actual neural firing patterns?   

  8. How can we think about the many feedback connections (often skipping layers) during recognition/classification tasks (not during the learning phase)? Similar for the feedforward connections that skip layers.   


