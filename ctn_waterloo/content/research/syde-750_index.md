title: SYDE 556/750 - Simulating Neurobiological Systems
picture: http://i.imgur.com/f5JyChE.png
intro: >
    Materials for a systems design engineering course offered by Professor Eliasmith.
    Includes notes, assignments, projects, slides, etc.
people:
    - Chris Eliasmith
    - Terry Stewart
toc:
    - Matlab Tutorial for SYDE 556
    - SYDE 556 Course Outline
    - SYDE 556 Possible Projects

#  SYDE 556: Simulating Neurobiological Systems

[Course outline](/research/syde-750/syde-556-course-outline.html)

Supporting Instructor: Terry Stewart ([Email](mailto:terry.stewart@gmail.com))

Office: PAS 2463

Office Hours: Monday 12:30-1:30, or by appointment

_Important Date:_ Mar 20: van der Meer Lab Tour - meet at the regular room

_Important Date:_ Mar 25: Project Presentations

_Presentation Order_: Peter Suma; Wen Yu; Lucas Rezek; Brent Komer; Angela
Kim; Suhaila Baheyeldin; Mengxi Zhu; Ben Selby; Peter Blouw; Wilten Nicola;
Oliver Trujillo; Edith Chow; Naz Sepahvand; Ivana Kajich; Mohammad Badr; Jason
Pye & Laurence Pike; Nolan Finkelstein; Dan Nichol; Kevin Barton

* * *

## Lecture Notes

These are updated to the most recent versions _after_ each lecture. Lecture
slides and notes are .pdf files.

[1: [.pdf slides](/files/syde-750/syde%20758.lecture1.pdf)]

[2: [notes](/files/syde-750/lecture2.pdf) /
[.pdf slides](/files/syde-750/syde%20758.lecture2.pdf)]

[3: [notes](/files/syde-750/lecture3.pdf) /
[.pdf slides](/files/syde-750/syde%20758.lecture3.pdf)]

[4: [notes](/files/syde-750/lecture4.pdf) /
[.pdf slides](/files/syde-750/syde%20758.lecture4.pdf)]

[5: [notes](/files/syde-750/lecture5.pdf) /
[.pdf slides](/files/syde-750/syde%20758.lecture5.pdf)]

[6: [notes](/files/syde-750/lecture6.pdf) /
[.pdf slides](/files/syde-750/syde%20758.lecture6.pdf)]

[7: [notes](/files/syde-750/lecture7.pdf) /
[.pdf slides](/files/syde-750/syde%20758.lecture7.pdf)]

[8: [notes](/files/syde-750/lecture8.pdf) /
[.pdf slides](/files/syde-750/syde%20758.lecture8.pdf)]

[9: [notes](/files/syde-750/lecture9.pdf) /
[.pdf slides](/files/syde-750/syde%20758.lecture9.pdf)]

[10: [notes](/files/syde-750/lecture10.pdf) /
[.pdf slides](/files/syde-750/syde%20758.lecture10.pdf)]

* * *

##  Coding Exercises by Lecture Number

* [[Matlab tutorial](/research/syde-750/matlab-tutorial-for-syde-556.html)]
* [[Exercise 2](/files/syde-750/exercises2.pdf) (2 weeks) 20 marks] due: Jan 30
* [[Exercise 3](/files/syde-750/exercises3.pdf) (2 weeks; see hint below) 20 marks] due: Feb 25
* [[Exercise 5](/files/syde-750/exercises5.pdf) (2 weeks) 10 marks] due: Mar 14
* [[Exercise 8](/files/syde-750/exercises8_nengo.pdf) (1 week) 10 marks] due: Mar 21 ([Dowload Nengo](http://nengo.ca/))

_Solutions_: If you would like solutions for any exercises, please [email
me](mailto:celiasmith@uwaterloo.ca).

Here's an example Nengo script we developed in class, building a simple
creature that can move in different directions, keep track of where it is, and
run back to its starting point when told to:
[creature.py](/files/syde-750/creature.py)

* Do not copy any code, you are expected to write your own code from scratch for this course.
* Please hand in electronic copies by mailing them to me in .pdf format. Include code, or any modified code. Please name the document like this: `<lastname>.Assignment<assn. #>.pdf`
* Uncommented genSignal code for lecture 3 & 4 is [here](/files/syde-750/genSignal.m) -- try writing it on your own first.
* The uncommented optimal filter code for lecture 3 & 4 is [here](/files/syde-750/optimal_filters_uncommented.m).
* For 556/750, exercise 3, if you get stuck on the first question, look near the end of the code.
* For Exercise 5: The code to compute the Gamma matrix (called CMatrix in the code) is [here](/files/syde-750/genCMatrix.m). When using this code, two variables, `Cmatrix` and `Moments` are returned. `Cmatrix` is the same as Gamma (with no noise) and `Moments(:,2)` is `V` (upsilon) [or, more accurately, unscaled `V` in higher dimensions, i.e. `V = Moments(:,2) * ones(1,D) .* EncVec`]. Be sure to use these moments and not your own calculation of `V` (since the former has been scaled appropriately). (If you need genActivities -- I'd encourage you to first try on your own -- it can be found [here](/files/syde-750/genActivities.m)).
* Please hand in your code and the requested plots and answers to questions electronically.
* Exercises are due one or two weeks after they are assigned (as noted). They are due by midnight that day. After that, one mark per day will be lost.

* * *

## Project Ideas

This [list](/research/syde-750/syde-556-possible-projects.html) is not intended to be comprehensive.
Please have your projects approved by me by the beginning of Feb. at the
latest.

### Project Format

The project report should be in the format discussed in chapter 1 of the book
(see pp. 19-23; i.e., System Description, Design Specification,
Implementation). Students will also be expected to do a short (15min)
presentation on your topic in the last weeks. As with assignments, all code
must be submitted as well.

* * *

## Course Format

Two lectures per week and homework assignments consisting of computer
exercises using Matlab. For SYDE 750 a class project is required, usually a
computer simulation developed based on significant neuroscientific research
and/or collaboration with a neurophysiologist. For Syde 556 a class project
based on an in class/text example is required. This course examines a general
framework for modeling computation by neurobiological systems with an emphasis
on quantitative formulations. Particular emphasis will be placed on
understanding computation, representation, and dynamics in such systems.
Students will learn how the fundamentals of signal processing, control theory
and statistical inference, can be applied to modeling sensory, motor, and
cognitive systems.

* * *

## Course Prerequisites

Knowing how to program using MATLAB is highly recommended. Familiarity with
Fourier Transforms and other signal processing concepts is recommended.
Familiarity with calculus and linear algebra is required.

* * *

## Useful Links

Matlab

* [Mathworks](http://www.mathworks.com/) (makers of Matlab)
* [Matlab Tutorial](NEFcourse/matlabTutorial) (Eliasmith)

Computational Neuroscience

* [Lecture notes on biologically realistic neural modeling (GENESIS) ](http://www.genesis-sim.org/GENESIS/)
* [Book overviews](NEFcourse/bookComments) (Eliasmith)
* [Journal of Computational Neuroscience](http://webdev.uwaterloo.ca/ejournals/stats?ejournal_id=7213&navbar=uw&navbase=tug.lib.uwaterloo.ca)
* [Neural Computation](http://webdev.uwaterloo.ca/ejournals/stats?ejournal_id=4796&navbar=uw&navbase=tug.lib.uwaterloo.ca)

Neuroscience

* [Digital Anatomist Atlas](http://www9.biostr.washington.edu/da.html) (Neuroanatomy)
* [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi) (Find neuro and related articles)
* [ Journal of Neuroscience](http://webdev.uwaterloo.ca/ejournals/stats?ejournal_id=3870&navbar=uw&navbase=tug.lib.uwaterloo.ca)
* [Nature Neuroscience](http://webdev.uwaterloo.ca/ejournals/stats?ejournal_id=9650&navbar=uw&navbase=tug.lib.uwaterloo.ca)
* [Science](http://webdev.uwaterloo.ca/ejournals/stats?ejournal_id=7892&navbar=uw&navbase=tug.lib.uwaterloo.ca)
* [Nature](http://webdev.uwaterloo.ca/ejournals/stats?ejournal_id=7884&navbar=uw&navbase=tug.lib.uwaterloo.ca)
* [Annual Review of Neuroscience](http://webdev.uwaterloo.ca/ejournals/stats?ejournal_id=386&navbar=uw&navbase=tug.lib.uwaterloo.ca)
* [Current Opinion in Neurobiology](http://webdev.uwaterloo.ca/ejournals/stats?ejournal_id=1627&navbar=uw&navbase=tug.lib.uwaterloo.ca)
* [Journal of Cognitive Neuroscience](http://webdev.uwaterloo.ca/ejournals/stats?ejournal_id=3419&navbar=uw&navbase=tug.lib.uwaterloo.ca)
* [Trends in Neuroscience](http://webdev.uwaterloo.ca/ejournals/stats?ejournal_id=6271&navbar=uw&navbase=tug.lib.uwaterloo.ca)
* [Trends in Cognitive Science](http://webdev.uwaterloo.ca/ejournals/stats?ejournal_id=6264&navbar=uw&navbase=tug.lib.uwaterloo.ca)
* [Jove: Visualized Experiments](http://www.jove.com/index/browse.stp?Tag=Neuroscience&sn=BID21) (very cool)
* [A Longer List of Neuro Journals](http://thalamus.wustl.edu/journals.html)
* [A nice introductory brain chapter](http://williamcalvin.com/bk7/bk7ch6.htm)
