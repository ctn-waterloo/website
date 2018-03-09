title: SYDE 556/750 - Simulating Neurobiological Systems
picture: http://i.imgur.com/f5JyChE.png
intro: >
    Course information for SYDE 556/750, taught Winter 2018.
people:
    - Chris Eliasmith
    - Terry Stewart
toc:
    - SYDE 556 Course Outline
    - SYDE 556 Possible Projects
    - Matlab Tutorial for SYDE 556

#  SYDE 556: Simulating Neurobiological Systems

[Course outline](/courses/syde-750/syde-556-course-outline.html)

_Instructor:_ Terry Stewart ([tcstewar@uwaterloo.ca](mailto:tcstewar@uwaterloo.ca))

_Office:_ PAS 2463

_Office Hours:_ Monday 2-3 and Thursday 3-4, or by appointment

_Location:_ E5 6127

_Times:_ Mon 12:00pm-1:20pm & Thurs. 12:30p-1:50p (plus 2:00p-2:50p Thurs for SYDE 750)

_Due Dates:_ 

 * Jan 22rd: Assignment #1 (due at midnight) (20%)
 * Feb 17th: Assignment #2 (due at midnight) (20%) 
 * Mar 12th: Assignment #3 (due at midnight) (10%)
 * Mar 19th: Assignment #4 (due at midnight) (10%)
 * Apr 19th: Final Project (40%)


* * *

## Lecture Notes

The in-class lecture notes will be posted here before each class.

 * Week 1: (January 4) [Introduction](http://nbviewer.ipython.org/github/tcstewar/syde556-1/blob/master/SYDE%20556%20Lecture%201%20Introduction.ipynb)
 * Week 2: (January 8, 11) [Representation](http://nbviewer.ipython.org/github/tcstewar/syde556-1/blob/master/SYDE%20556%20Lecture%202%20Representation.ipynb)
 * Week 3: (January 15, 18) [Temporal Representation](http://nbviewer.ipython.org/github/tcstewar/syde556-1/blob/master/SYDE%20556%20Lecture%203%20Temporal%20Representation.ipynb)
 * Week 4: (January 22, 25) [Transformation](http://nbviewer.ipython.org/github/tcstewar/syde556-1/blob/master/SYDE%20556%20Lecture%204%20Transformation.ipynb)
 * Week 5, 6: (January 29, Feb 1, 5, 8) [Dynamics](http://nbviewer.ipython.org/github/tcstewar/syde556-1/blob/master/SYDE%20556%20Lecture%205%20Dynamics.ipynb)

   * [Critter Example](https://github.com/tcstewar/syde556-1/blob/master/critter.py)

 * Week 7: (Feb 12, 15) [Final Project](http://nbviewer.jupyter.org/github/tcstewar/syde556-1/blob/master/Final%20Projects.ipynb), [Symbols](http://nbviewer.jupyter.org/github/tcstewar/syde556-1/blob/master/SYDE%20556%20Lecture%207%20Symbols.ipynb)
 * Week 8: (Feb 26) [Action Selection](http://nbviewer.jupyter.org/github/tcstewar/syde556-1/blob/master/SYDE%20556%20Lecture%209%20Action%20Selection.ipynb)
 * Week 9: (Mar 5) [Learning](http://nbviewer.jupyter.org/github/tcstewar/syde556-1/blob/master/SYDE%20556%20Lecture%2010%20Learning.ipynb), [Memory Summary](https://nbviewer.jupyter.org/github/Seanny123/guest_syde556_lec/blob/master/Memory%20Summary.ipynb), [Large Scale Modelling](https://nbviewer.jupyter.org/github/Seanny123/guest_syde556_lec/blob/master/Scaling%20SPA%20for%20complex%20behaviour.ipynb)

* * *

##  Assignments

The four assignments will be posted here.

 * Do not copy any code from other students or online sources.  You are expected to write your own code from scratch for this course.
 * Each student must write their own code and submit their own assignment.
 * Please hand in electronic copies by mailing them to me in .pdf format.  Please name the document like this: `<lastname>.Assignment<number>.pdf`.  This document will have all the graphs and any written answers to questions. (From a jupyter notebook, you can do ```jupyter nbconvert --to pdf my_name.assignment1.ipynb```)
 * Include code, or any modified code, in a second document as well.  This should be in a single file (e.g. .zip) named similarly: `<lastname>.Assignment<numnber>.Code.zip`
 * Assignments are due _at Midnight_.  The late penalty is one mark per day it is late.

 * Assignment 1: (due January 22nd) [Assignment 1](http://nbviewer.ipython.org/github/tcstewar/syde556-1/blob/master/Assignment%201.ipynb)
 * Assignment 2: (due February 17th) [Assignment 2](http://nbviewer.ipython.org/github/tcstewar/syde556-1/blob/master/Assignment%202.ipynb)
 * Assignment 3: (due March 12th) [Assignment 3](http://nbviewer.ipython.org/github/tcstewar/syde556-1/blob/master/Assignment%203.ipynb)
  
* * *

## Project Ideas

The final project for the course consists of picking a neurobiological system and
building a model for it.  There is a list of possible projects and more info at [http://nbviewer.jupyter.org/github/tcstewar/syde556-1/blob/master/Final%20Projects.ipynb](http://nbviewer.jupyter.org/github/tcstewar/syde556-1/blob/master/Final%20Projects.ipynb),
but is not intended to be comprehensive, so feel free to come up with your own ideas.
Please have your projects approved by me by the end of Reading Week.  You will need to submit a short (3-paragraph) summary of your project by March 29th.

### Project Format

The project report should be in the format discussed in chapter 1 of the book
(see pp. 19-23; i.e., System Description, Design Specification,
Implementation). Students will also be expected to do a short (5-10min)
presentation on your topic in the last week or so.  That presentation should consist of a few slides (max 4), that sets up the problem and describes your expected approach. As with assignments, all code for projects must be submitted as well.

* * *

## Course Format

Two lectures per week and homework assignments consisting of computer
exercises using Python (or Matlab). For SYDE 750 a larger class project is required, usually a
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

Knowing how to program with matrices using Python, Matlab or some other language is highly 
recommended. Familiarity with Fourier Transforms and other signal processing concepts is recommended.
Familiarity with calculus and linear algebra is required.

* * *

## Useful Links

Programming

* [NumPy for MATLAB users](http://wiki.scipy.org/NumPy_for_Matlab_Users) (a good quick reference for common matrix operations, comparing both Python and Matlab)
* [Mathworks](http://www.mathworks.com/) (makers of Matlab)
* [Matlab Tutorial](/courses/syde-750/matlab-tutorial-for-syde-556.html) (Eliasmith)

Computational Neuroscience

* [Lecture notes on biologically realistic neural modeling (GENESIS) ](http://www.genesis-sim.org/GENESIS/)
* [Book overviews](/research/theoretical-neuroscience/comments-on-theoretical-neuroscience-books.html) (Eliasmith)
* [Journal of Computational Neuroscience](http://webdev.uwaterloo.ca/ejournals/stats?ejournal_id=7213&navbar=uw&navbase=tug.lib.uwaterloo.ca)
* [Neural Computation](http://webdev.uwaterloo.ca/ejournals/stats?ejournal_id=4796&navbar=uw&navbase=tug.lib.uwaterloo.ca)

Neuroscience

* [Digital Anatomist Atlas](http://www9.biostr.washington.edu/da.html) (Neuroanatomy)
* [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi) (Find neuro and related articles)
* [Journal of Neuroscience](http://webdev.uwaterloo.ca/ejournals/stats?ejournal_id=3870&navbar=uw&navbase=tug.lib.uwaterloo.ca)
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
