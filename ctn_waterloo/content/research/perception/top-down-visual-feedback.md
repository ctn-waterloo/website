title: Top-down visual feedback

Feel free to correct, comment, or suggest any thoughts or ideas.

Principle Investigator: Charlie Tang; [Project Status](?q=node/523)

## Project: Top-down feedback for segmentation in vision

Recent advances in "deep" hierarchical modeling inspired by the cortex are
exciting. There are two main types of deep architectures. One is based on
generative, probabilistic modeling of the sensory data (Hinton's group). The
other is of a feedforward discriminative and/or sparse coding type of model
(Le Cun's group). Both can be adapted to a semi-supervised framework as well.

There are massive feedback connections present in the cortex. Deep belief
network use feedback as part of the likelihood function p(v|h) as well as
setting a prior on h. Therefore, it uses feedback to "imagine" sensory data.

There are still questions left to be asked. First, is the brain really a
probabilistic model with each neural populations representing one random
variable? And what about top-down projections which skip down multiple layers?
Second, for recognition, most existing deep networks use 1 forward propagation
in a discriminative framework. The fact that no feedback is incorporated in
the model is often justified by the task at hand, which is simple
categorization detection, or recognition. Though the jury is still out on
whether recognition needs feedback or not, it is likely to be the case that
segmentation of objects/digits/faces need feedback connections. This is the
main focus of the project.

## Learning about deep learning - Questions

  * what is the expressiveness of a simple RBM model, what is the complexity of the pdf it can model?
  * why does pretraining (unsupervised modeling of data distribution) help fine tuning in a deep feedforward network?
