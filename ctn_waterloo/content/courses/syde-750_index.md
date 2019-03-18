title: SYDE 556/750 - Simulating Neurobiological Systems
picture: http://i.imgur.com/f5JyChE.png
intro: >
    Course information for SYDE 556/750, taught Winter 2019.
people:
    - Chris Eliasmith
    - Terry Stewart
toc:
    - SYDE 556 Course Outline
    - SYDE 556 Possible Projects
    - Matlab Tutorial for SYDE 556

#  SYDE 556: Simulating Neurobiological Systems

[Course outline](/courses/syde-750/syde-556-course-outline.html)

_Instructor:_ Chris Eliasmith ([celiasmith@uwaterloo.ca](mailto:celiasmith@uwaterloo.ca))

_Office:_ E7 6324

_Office Hours:_ By appointment

_TA:_ Andreas Stoeckel ([astoeckel@uwaterloo.ca](mailto:astoeckel@uwaterloo.ca))

_Office:_ E7 6321

_Office Hours:_ By appointment

_Class Location:_ Mon: E5-6004, Wed: E7-5343

_Times:_ Mon 9:00a-10:20a & Wed. 9:00a-10:20a (plus 10:30a-11:30p Wed for SYDE 750)

_Due Dates:_ 

 * Jan 28th: Assignment #1 (due at midnight) (20%)
 * Feb 15th: Assignment #2 (due at midnight) (20%) 
 * Mar 6th: Assignment #3 (due at midnight) (10%)
 * Mar 20th: Assignment #4 (due at midnight) (10%)
 * Apr 18th: Final Project (40%)


* * *

## Lecture Notes

The in-class lecture notes will be posted here before each class.

 * Week 1: (January 7) [Introduction](https://github.com/celiasmith/syde556/blob/master/SYDE%20556%20Lecture%201%20Introduction.ipynb)
 * Week 2: (January 9, 14) [Representation](https://github.com/celiasmith/syde556/blob/master/SYDE%20556%20Lecture%202%20Representation.ipynb)
 * Week 3: (January 16, 21) [Temporal Representation](https://github.com/celiasmith/syde556/blob/master/SYDE%20556%20Lecture%203%20Temporal%20Representation.ipynb)
 * Week 4, 5: (January 23, 28, 30) [Transformation](https://github.com/celiasmith/syde556/blob/master/SYDE%20556%20Lecture%204%20Transformation.ipynb)
 * Week 5, 6: (Feb 4, 6, 11) [Dynamics](https://github.com/celiasmith/syde556/blob/master/SYDE%20556%20Lecture%205%20Dynamics.ipynb)
 * Week 7: (Feb 13, 25) [Analysis of Representation](https://github.com/celiasmith/syde556/blob/master/SYDE%20556%20Lecture%206%20Decoder%20Analysis.ipynb)
 * Week 8: (Feb 27, Mar 4) [Symbols](https://github.com/celiasmith/syde556/blob/master/SYDE%20556%20Lecture%207%20Symbols.ipynb)
 * Week 9: (Mar 6, 11) [Memory](https://github.com/celiasmith/syde556/blob/master/SYDE%20556%20Lecture%208%20Memory.ipynb)
 * Week 10: (Mar 13, 18) [Action Selection](https://github.com/celiasmith/syde556/blob/master/SYDE%20556%20Lecture%209%20Action%20Selection.ipynb)
 * Week 11: (Mar 20, 25) [Learning]

* * *

##  Assignments

The four assignments will be posted here.

 * Do not copy any code from other students or online sources.  You are expected to write your own code from scratch for this course.
 * Each student must write their own code and submit their own assignment.
 * Please hand in electronic copies by mailing them to me in .pdf format.  Please name the document like this: `<lastname>.Assignment<number>.pdf`.  This document will have all the graphs and any written answers to questions. (From a jupyter notebook, you can do ```jupyter nbconvert --to pdf my_name.assignment1.ipynb```)
 * Include code, or any modified code, in a second document as well.  This should be in a single file (e.g. .zip) named similarly: `<lastname>.Assignment<numnber>.Code.zip`
 * Assignments are due _at Midnight_.  The late penalty is one mark per day it is late.

 * Assignment 1: (due January 28th) [Assignment 1](https://github.com/celiasmith/syde556/blob/master/Assignment%201.ipynb)
 * Assignment 2: (due February 15th) [Assignment 2](https://github.com/celiasmith/syde556/blob/master/Assignment%202.ipynb)
 * Assignment 3: (due March 6th) [Assignment 3](https://github.com/celiasmith/syde556/blob/master/Assignment%203.ipynb)
 * Assignment 4: (due March 20th) [Assignment 4](https://github.com/celiasmith/syde556/blob/master/Assignment%204.ipynb)
  
* * *

## Project Ideas

The final project for the course consists of picking a neurobiological system and
building a model for it.  There is a list of possible projects and more info at [this link](http://compneuro.uwaterloo.ca/courses/syde-750/syde-556-possible-projects.html),
but is not intended to be comprehensive, so feel free to come up with your own ideas.
Please have your projects approved by me by the end of Reading Week.  To do so, you will need to submit a short summary of your project by Feb 24th.

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

* [NumPy for MATLAB users](https://docs.scipy.org/doc/numpy-1.15.0/user/numpy-for-matlab-users.html) (a good quick reference for common matrix operations, comparing both Python and Matlab)
* [Mathworks](http://www.mathworks.com/) (makers of Matlab)
* [Matlab Tutorial](/courses/syde-750/matlab-tutorial-for-syde-556.html) (Eliasmith)

Computational Neuroscience

* [Lecture notes on biologically realistic neural modeling (GENESIS) ](http://www.genesis-sim.org/GENESIS/)
* [Book overviews](/research/theoretical-neuroscience/comments-on-theoretical-neuroscience-books.html) (Eliasmith)
* [Journal of Computational Neuroscience](https://sfx.scholarsportal.info/waterloo?ctx_ver=Z39.88-2004&ctx_enc=info:ofi/enc:UTF-8&ctx_tim=2019-01-08T14%3A03%3A43IST&url_ver=Z39.88-2004&url_ctx_fmt=infofi/fmt:kev:mtx:ctx&rfr_id=info:sid/primo.exlibrisgroup.com:primo3-Journal-vtug&rft_val_fmt=info:ofi/fmt:kev:mtx:journal&rft.genre=&rft.atitle=&rft.jtitle=Journal%20of%20computational%20neuroscience&rft.btitle=&rft.aulast=&rft.auinit=&rft.auinit1=&rft.auinitm=&rft.ausuffix=&rft.au=&rft.aucorp=&rft.volume=&rft.issue=&rft.part=&rft.quarter=&rft.ssn=&rft.spage=&rft.epage=&rft.pages=&rft.artnum=&rft.issn=0929-5313&rft.eissn=&rft.isbn=&rft.sici=&rft.coden=&rft_id=info:doi/&rft.object_id=&svc_val_fmt=info:ofi/fmt:kev:mtx:sch_svc&rft.eisbn=&rft_dat=%3Cvtug%3E3297598%3C/vtug%3E%3Cgrp_id%3E646505283%3C/grp_id%3E%3Coa%3E%3C/oa%3E%3Curl%3E%3C/url%3E&rft_id=info:oai/&req.language=eng&rft_pqid=)
* [Neural Computation](https://primo.tug-libraries.on.ca/primo_library/libweb/action/dlDisplay.do?docId=dedupmrg406056967&institution=WATERLOO&vid=WATERLOO&search_scope=books_tab&onCampus=false&indx=1&bulkSize=2&dym=true&highlight=true&lang=eng&group=GUEST&query=any,contains,neural%20computation%20journal)
* [PLoS Computational Biology](https://journals.plos.org/ploscompbiol/)

Neuroscience

* [Digital Anatomist Atlas](http://www9.biostr.washington.edu/da.html) (Neuroanatomy)
* [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi) (Find neuro and related articles)
* Journals:
    * Journal of Neuroscience
    * Nature Neuroscience
    * Annual Review of Neuroscience
    * Current Opinion in Neurobiology
    * Journal of Cognitive Neuroscience
    * Trends in Neuroscience
    * Trends in Cognitive Science
* [Jove: Visualized Experiments](http://www.jove.com/index/browse.stp?Tag=Neuroscience&sn=BID21) (very cool)
* [A nice introductory brain chapter](http://williamcalvin.com/bk7/bk7ch6.htm)
