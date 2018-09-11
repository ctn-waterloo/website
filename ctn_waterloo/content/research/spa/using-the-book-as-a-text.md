title: Using the book as a text

Given the practical nature of much of the material in the book,
it can be used quite successfully as a textbook
for a course on cognitive or neural modelling.
The material below will assist instructors in running such a course.

.. note:: If you are looking for something specific
          (e.g. specific slides, images, code, etc.),
          please do not hesitate to contact
          `Chris Eliasmith <mailto:celiasmith@uwaterloo.ca>`_.

Suggested lecture schedule
==========================

I've provided more lectures
than I believe you can fit in a single term.
However, this allows lecturers to
add and remove topics as they see fit,
or change the emphasis of a particular version of the course.
I'm assuming that each lecture is
3 hours (i.e. a typical week's worth of material).

+------------+----------------+------------------------------+--------------------+
| Lecture    | Readings       | Topics                       | Assignment         |
+============+================+==============================+====================+
| Week 1     | Sections       | * A brief history            | Install and        |
|            | 1.1 & 1.2:     |   of cognitive science       | run Nengo          |
|            | The Science    | * Central features           |                    |
|            | of Cognition   |   of the main approaches     |                    |
+------------+----------------+------------------------------+--------------------+
| Week 2     | Sections       | * Challenges for             | Build a model of   |
|            | 1.3 & 1.4      |   cognitive science          | a single neuron    |
|            |                | * Overview of the approach   |                    |
|            |                |   in this course             |                    |
+------------+----------------+------------------------------+--------------------+
| Week 3     | Sections       | * An introduction to         | Build a model of   |
|            | 2.2 & 2.2.1    |   basic neurophysiology      | 1D representation  |
|            |                |   and anatomy                |                    |
|            |                | * Principle 1 of the NEF:    |                    |
|            |                |   representation             |                    |
+------------+----------------+------------------------------+--------------------+
| Week 4     | Section 2.2.2  | * Principle 2 of the NEF:    | Build a model that |
|            |                |   computation                | computes linear    |
|            |                |                              | and nonlinear      |
|            |                |                              | functions of a     |
|            |                |                              | single variable    |
+------------+----------------+------------------------------+--------------------+
| Week 5     | Section 2.2.3  | * Principle 3 of the NEF:    | Build a model of   |
|            |                |   dynamics                   | a 1D integrator    |
+------------+----------------+------------------------------+--------------------+
| Week 6     | Section 2.6    | * Levels of description in   | Build a model      |
| (optional) |                |   the behavioral sciences    | at 3 levels        |
|            |                |                              | of description     |
+------------+----------------+------------------------------+--------------------+
| Week 7     | Sections       | * Overview of the semantic   | Build a model of   |
|            | 3.1--3.4       |   pointer hypothesis         | 2D (or higher-D)   |
|            |                | * Distributed neural         | representation     |
|            |                |   semantics                  |                    |
+------------+----------------+------------------------------+--------------------+
| Week 8     | Sections       | * An introduction to         | Build a model of   |
|            | 3.5--3.7       |   visual semantics           | 2D nonlinear       |
|            |                | * An introduction to         | computation        |
|            |                |   motor semantics            | (multiplication)   |
+------------+----------------+------------------------------+--------------------+
| Week 9     | Sections       | * Syntactic representations  | Build a binding    |
|            | 4.1--4.4 & 4.6 | * Vector symbolic            | neural network     |
|            |                |   architectures              |                    |
|            |                | * Implementations of VSAs    |                    |
|            |                |   in neurons                 |                    |
+------------+----------------+------------------------------+--------------------+
| Week 10    | Sections       | * Learning syntactic         | Build a model      |
| (optional) | 4.5--4.7       |   manipulations              | that learns an     |
|            |                | * Modeling fluid             | unknown syntactic  |
|            |                |   intelligence               | transformation     |
|            |                | * Syntax and semantics       |                    |
|            |                |   for structured concepts    |                    |
+------------+----------------+------------------------------+--------------------+
| Week 11    | Sections       | * Basal ganglia              | Build a basal      |
|            | 5.1--5.3       |   anatomy and physiology     | ganglia model      |
|            |                | * Basal ganglia function     | that selects       |
|            |                |                              | among 5 actions    |
+------------+----------------+------------------------------+--------------------+
| Week 12    | Sections       | * Basal ganglia use for      | Build a question   |
|            | 5.4, 5.6--5.8  |   flexible action selection  | answering model    |
|            |                | * Example uses of the basal  | with control       |
|            |                |   ganglia model in the SPA   |                    |
+------------+----------------+------------------------------+--------------------+
| Week 13    | Sections       | * Introduction to cognition  | Build a (serial)   |
|            | 6.1--6.3       |   through time               | working memory     |
|            |                | * Working memory and         | model              |
|            |                |   serial working memory      |                    |
+------------+----------------+------------------------------+--------------------+
| Week 14    | Sections       | * Spike-timing dependent     | Build a network    |
|            | 6.4--6.6       |   plasticity (STDP)          | that learns an     |
|            |                | * Reinforcement learning     | arbitrary 1D       |
|            |                | * Learning transformations   | transformation     |
|            |                |   with the hPES rule         |                    |
+------------+----------------+------------------------------+--------------------+
| Week 15    | Sections       | * A review and overview      | Build a question   |
|            | 7.1--7.3       |   of the SPA                 | answering model    |
|            |                | * The Spaun model and tasks  | with control       |
+------------+----------------+------------------------------+--------------------+
| Week 16    | Section 7.4    | * Probabilistic models       | Build a model      |
| (optional) |                | * Interpreting the SPA       | to do a simple     |
|            |                |   as a probabilistic model   | statistical        |
|            |                |                              | inference problem  |
+------------+----------------+------------------------------+--------------------+
| Week 17    | Chapter 8      | * Evaluating cognitive       | Begin a course     |
|            |                |   theories                   | project, using     |
|            |                | * Detailed discussion of the | tutorial 8         |
|            |                |   core cognitive criteria    | as an example      |
+------------+----------------+------------------------------+--------------------+
| Week 18    | Chapter 9      | * A survey of other          | Course project     |
|            |                |   approaches to cognitive    |                    |
|            |                |   modelling                  |                    |
|            |                | * A comparison of the SPA    |                    |
|            |                |   with past approaches       |                    |
+------------+----------------+------------------------------+--------------------+
| Week 19    | Chapter 10     | * Conceptual consequences of | Course project     |
|            |                |   the SPA and NEF methods    |                    |
|            |                | * Future challenges for this |                    |
|            |                |   and other approaches       |                    |
+------------+----------------+------------------------------+--------------------+

Assignment details
==================

The assignments above mirror those in the book.
It is also useful to ask questions
about the functioning of the models being built,
and to ask students to change the models slightly
to examine different aspects of neural/cognitive processing.
The intent of this section of the website
is to provide examples of such questions,
as we develop them.
`Suggestions welcome <forum_>`_.

Suggested projects
==================

* Build a creature to seek food and return to a home nest.

* Build a serial working memory model that allows for loading, reset, etc.

* Build a robot controller for a robot
  that you present instructions to,
  that it memorizes and then executes.

* Build an adaptive controller for a 3-link arm
  using Slotine's adaptation methods.

* Build a model that does any one of the tasks in Spaun.

* Build something on the `modelling ideas list <ideas_>`_.

If you have a project suggestions,
please add it to the `modelling ideas list <ideas_>`_,
or post it `on the forum <forum_>`_.

.. _ideas: https://github.com/ctn-waterloo/modelling_ideas/issues

.. _forum: https://forum.nengo.ai/
