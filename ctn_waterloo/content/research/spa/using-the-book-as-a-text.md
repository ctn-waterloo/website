title: Using the book as a text

Given the practical nature of much of the material in the book,
it can be used quite successfully as a textbook
for a course on cognitive or neural modelling.
The material below will assist instructors in running such a course.

Note: If you are looking for something specific
          (e.g. specific slides, images, code, etc.),
          please do not hesitate to contact
          Chris Eliasmith <celiasmith@uwaterloo.ca>.

## Suggested lecture schedule

I've provided more lectures
than I believe you can fit in a single term.
However, this allows lecturers to
add and remove topics as they see fit,
or change the emphasis of a particular version of the course.
I'm assuming that each lecture is
3 hours (i.e. a typical week's worth of material).

<table border="1" class="docutils">
<colgroup>
<col width="15%" />
<col width="21%" />
<col width="38%" />
<col width="26%" />
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Lecture</th>
<th class="head">Readings</th>
<th class="head">Topics</th>
<th class="head">Assignment</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>Week 1</td>
<td>Sections
1.1 &amp; 1.2:
The Science
of Cognition</td>
<td><ul class="first last simple">
<li>A brief history
of cognitive science</li>
<li>Central features
of the main approaches</li>
</ul>
</td>
<td>Install and
run Nengo</td>
</tr>
<tr class="row-odd"><td>Week 2</td>
<td>Sections
1.3 &amp; 1.4</td>
<td><ul class="first last simple">
<li>Challenges for
cognitive science</li>
<li>Overview of the approach
in this course</li>
</ul>
</td>
<td>Build a model of
a single neuron</td>
</tr>
<tr class="row-even"><td>Week 3</td>
<td>Sections
2.2 &amp; 2.2.1</td>
<td><ul class="first last simple">
<li>An introduction to
basic neurophysiology
and anatomy</li>
<li>Principle 1 of the NEF:
representation</li>
</ul>
</td>
<td>Build a model of
1D representation</td>
</tr>
<tr class="row-odd"><td>Week 4</td>
<td>Section 2.2.2</td>
<td><ul class="first last simple">
<li>Principle 2 of the NEF:
computation</li>
</ul>
</td>
<td>Build a model that
computes linear
and nonlinear
functions of a
single variable</td>
</tr>
<tr class="row-even"><td>Week 5</td>
<td>Section 2.2.3</td>
<td><ul class="first last simple">
<li>Principle 3 of the NEF:
dynamics</li>
</ul>
</td>
<td>Build a model of
a 1D integrator</td>
</tr>
<tr class="row-odd"><td>Week 6
(optional)</td>
<td>Section 2.6</td>
<td><ul class="first last simple">
<li>Levels of description in
the behavioral sciences</li>
</ul>
</td>
<td>Build a model
at 3 levels
of description</td>
</tr>
<tr class="row-even"><td>Week 7</td>
<td>Sections
3.1–3.4</td>
<td><ul class="first last simple">
<li>Overview of the semantic
pointer hypothesis</li>
<li>Distributed neural
semantics</li>
</ul>
</td>
<td>Build a model of
2D (or higher-D)
representation</td>
</tr>
<tr class="row-odd"><td>Week 8</td>
<td>Sections
3.5–3.7</td>
<td><ul class="first last simple">
<li>An introduction to
visual semantics</li>
<li>An introduction to
motor semantics</li>
</ul>
</td>
<td>Build a model of
2D nonlinear
computation
(multiplication)</td>
</tr>
<tr class="row-even"><td>Week 9</td>
<td>Sections
4.1–4.4 &amp; 4.6</td>
<td><ul class="first last simple">
<li>Syntactic representations</li>
<li>Vector symbolic
architectures</li>
<li>Implementations of VSAs
in neurons</li>
</ul>
</td>
<td>Build a binding
neural network</td>
</tr>
<tr class="row-odd"><td>Week 10
(optional)</td>
<td>Sections
4.5–4.7</td>
<td><ul class="first last simple">
<li>Learning syntactic
manipulations</li>
<li>Modeling fluid
intelligence</li>
<li>Syntax and semantics
for structured concepts</li>
</ul>
</td>
<td>Build a model
that learns an
unknown syntactic
transformation</td>
</tr>
<tr class="row-even"><td>Week 11</td>
<td>Sections
5.1–5.3</td>
<td><ul class="first last simple">
<li>Basal ganglia
anatomy and physiology</li>
<li>Basal ganglia function</li>
</ul>
</td>
<td>Build a basal
ganglia model
that selects
among 5 actions</td>
</tr>
<tr class="row-odd"><td>Week 12</td>
<td>Sections
5.4, 5.6–5.8</td>
<td><ul class="first last simple">
<li>Basal ganglia use for
flexible action selection</li>
<li>Example uses of the basal
ganglia model in the SPA</li>
</ul>
</td>
<td>Build a question
answering model
with control</td>
</tr>
<tr class="row-even"><td>Week 13</td>
<td>Sections
6.1–6.3</td>
<td><ul class="first last simple">
<li>Introduction to cognition
through time</li>
<li>Working memory and
serial working memory</li>
</ul>
</td>
<td>Build a (serial)
working memory
model</td>
</tr>
<tr class="row-odd"><td>Week 14</td>
<td>Sections
6.4–6.6</td>
<td><ul class="first last simple">
<li>Spike-timing dependent
plasticity (STDP)</li>
<li>Reinforcement learning</li>
<li>Learning transformations
with the hPES rule</li>
</ul>
</td>
<td>Build a network
that learns an
arbitrary 1D
transformation</td>
</tr>
<tr class="row-even"><td>Week 15</td>
<td>Sections
7.1–7.3</td>
<td><ul class="first last simple">
<li>A review and overview
of the SPA</li>
<li>The Spaun model and tasks</li>
</ul>
</td>
<td>Build a question
answering model
with control</td>
</tr>
<tr class="row-odd"><td>Week 16
(optional)</td>
<td>Section 7.4</td>
<td><ul class="first last simple">
<li>Probabilistic models</li>
<li>Interpreting the SPA
as a probabilistic model</li>
</ul>
</td>
<td>Build a model
to do a simple
statistical
inference problem</td>
</tr>
<tr class="row-even"><td>Week 17</td>
<td>Chapter 8</td>
<td><ul class="first last simple">
<li>Evaluating cognitive
theories</li>
<li>Detailed discussion of the
core cognitive criteria</li>
</ul>
</td>
<td>Begin a course
project, using
tutorial 8
as an example</td>
</tr>
<tr class="row-odd"><td>Week 18</td>
<td>Chapter 9</td>
<td><ul class="first last simple">
<li>A survey of other
approaches to cognitive
modelling</li>
<li>A comparison of the SPA
with past approaches</li>
</ul>
</td>
<td>Course project</td>
</tr>
<tr class="row-even"><td>Week 19</td>
<td>Chapter 10</td>
<td><ul class="first last simple">
<li>Conceptual consequences of
the SPA and NEF methods</li>
<li>Future challenges for this
and other approaches</li>
</ul>
</td>
<td>Course project</td>
</tr>
</tbody>
</table>


## Assignment details

The assignments above mirror those in the book.
It is also useful to ask questions
about the functioning of the models being built,
and to ask students to change the models slightly
to examine different aspects of neural/cognitive processing.
The intent of this section of the website
is to provide examples of such questions,
as we develop them.
[Suggestions welcome](https://forum.nengo.ai/).

## Suggested projects

* Build a creature to seek food and return to a home nest.

* Build a serial working memory model that allows for loading, reset, etc.

* Build a robot controller for a robot
  that you present instructions to,
  that it memorizes and then executes.

* Build an adaptive controller for a 3-link arm
  using Slotine's adaptation methods.

* Build a model that does any one of the tasks in Spaun.

* Build something on the [modelling ideas list](https://github.com/ctn-waterloo/modelling_ideas/issues).

If you have a project suggestions,
please add it to the [modelling ideas list](https://github.com/ctn-waterloo/modelling_ideas/issues),
or post it on [the Nengo forum](https://forum.nengo.ai/).

