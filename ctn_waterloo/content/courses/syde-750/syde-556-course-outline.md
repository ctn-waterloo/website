title: SYDE 556 Course Outline

## General Information

-   **Course title**  
    Simulating Neurobiological Systems (SYDE 556/750 topic 8)

-   **Course website**  
    Links to all course material, including slides and these lecture
    notes and slides can be found at the following URLs:

    -   <http://compneuro.uwaterloo.ca/courses/syde-750.html>

    -   <https://github.com/astoeckel/syde556-w20>

    *Note:* Any material on GitHub should be considered “preliminary”
    until officially linked at from the course website. Until then, the
    material is still subject to change.

-   **Instructor**  
    Andreas Stöckel  
    Office: E7-6342 (office hours in E7-6323)  
    Email: [astoecke@uwaterloo.ca](astoecke@uwaterloo.ca)  
    Website:
    <http://compneuro.uwaterloo.ca/people/andreas-stoeckel.html>

-   **Course times and location**

    -   Tuesday: 11:30-12:50 in E5-4106 (SYDE 556/750)

    -   Thursday: 9:00-10:20 in E5-6004 (SYDE 556/750)

    -   Thursday: 10:30-11:20 in E5-6127 (SYDE 750, optional for 556)

-   **Office hours**

    -   Office hours are generally in E7-6323 (this is a larger
        conference room).

    -   Time yet to be determined, one fixed office hour per week.

    -   Alternatively, if that time doesn’t work for you, by
        appointment.

-   **Readings**

    -   Main resource: “Neural Engineering: Representation, Computation and Dynamics in Neurobiological Systems”, Chris Eliasmith and Charles Anderson, 2003. MIT Press.

    -   Optional: “How to Build a Brain”, Chris Eliasmith, 2012


-   **Course Description**  
    This course examines a general framework for modeling
    computation by neurobiological systems with an emphasis on quantitative
    formulations. Particular emphasis will be placed on understanding computation,
    representation, and dynamics in such systems. Students will learn how the
    fundamentals of signal processing, control theory and statistical inference,
    can be applied to modeling sensory, motor, and cognitive systems.

-   **Prerequisites:**  
    Knowing how to program using `numpy` in Python is highly recommended.  Familiarity with calculus and linear algebra is required.

## Schedule

*Note:* This schedule is preliminary and still subject to change.

<table style="border-spacing: 0.5em">
<thead>
<tr class="header">
<th style="text-align: left; border-bottom: 2px solid black"><strong>Date</strong></th>
<th style="text-align: left; border-bottom: 2px solid black"><strong>Reading</strong></th>
<th style="text-align: left; border-bottom: 2px solid black"><strong>Topic</strong></th>
<th style="text-align: left; border-bottom: 2px solid black"><strong>Assignments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<th colspan="4" style="font-size: 75%; padding-top: 1em; text-align:left; border-bottom: 1px solid black">WEEK 1</th>
</tr>
<tr class="even">
<td>Jan 7</td>
<td>Chapter 1</td>
<td>Introduction</td>
<td></td>
</tr>
<tr class="odd">
<td>Jan 9</td>
<td>Chapter 2</td>
<td>Neurons</td>
<td></td>
</tr>
<tr class="even">
<th colspan="4" style="font-size: 75%; padding-top: 1em; text-align:left; border-bottom: 1px solid black">WEEK 2</th>
</tr>
<tr class="odd">
<td>Jan 14</td>
<td>Chapter 2</td>
<td>Population Representation (I)</td>
<td>#1 posted</td>
</tr>
<tr class="even">
<td>Jan 16</td>
<td>Chapter 2</td>
<td>Population Representation (II)</td>
<td></td>
</tr>
<tr class="odd">
<th colspan="4" style="font-size: 75%; padding-top: 1em; text-align:left; border-bottom: 1px solid black">WEEK 3</th>
</tr>
<tr class="even">
<td>Jan 21</td>
<td>Chapter 4</td>
<td>Temporal Representation (I)</td>
<td></td>
</tr>
<tr class="odd">
<td>Jan 23</td>
<td>Chapter 4</td>
<td>Temporal Representation (II)</td>
<td></td>
</tr>
<tr class="even">
<th colspan="4" style="font-size: 75%; padding-top: 1em; text-align:left; border-bottom: 1px solid black">WEEK 4</th>
</tr>
<tr class="odd">
<td>Jan 28</td>
<td>Chapters 5, 6</td>
<td>Feedforward Transformations (I)</td>
<td>#2 posted</td>
</tr>
<tr class="even">
<td>Jan 30</td>
<td>Chapters 5, 6</td>
<td>Feedforward Transformations (II)</td>
<td>#1 due*</td>
</tr>
<tr class="odd">
<th colspan="4" style="font-size: 75%; padding-top: 1em; text-align:left; border-bottom: 1px solid black">WEEK 5</th>
</tr>
<tr class="even">
<td>Feb 4</td>
<td>Chapter 8</td>
<td>Nengo Tutorial</td>
<td></td>
</tr>
<tr class="odd">
<td>Feb 6</td>
<td>Chapter 8</td>
<td>Dynamics (I)</td>
<td></td>
</tr>
<tr class="even">
<th colspan="4" style="font-size: 75%; padding-top: 1em; text-align:left; border-bottom: 1px solid black">WEEK 6</th>
</tr>
<tr class="odd">
<td>Feb 11</td>
<td>Chapter 8</td>
<td>Dynamics (II)</td>
<td>#3 posted</td>
</tr>
<tr class="even">
<td>Feb 13</td>
<td><em>see notes</em></td>
<td>Temporal Basis Functions</td>
<td>#2 due*</td>
</tr>
<tr class="odd">
<td>Feb 14</td>
<td></td>
<td></td>
<td>Project proposal due</td>
</tr>
<tr class="even">
<th colspan="4" style="font-size: 75%; padding-top: 1em; text-align:left; border-bottom: 1px solid black">WEEK 7</th>
</tr>
<tr class="even">
<td colspan="4" style="text-align: center; font-style: italic;">― Reading week, no lectures ―</td>
</tr>
<tr class="odd">
<th colspan="4" style="font-size: 75%; padding-top: 1em; text-align:left; border-bottom: 1px solid black">WEEK 8</th>
</tr>
<tr class="even">
<td>Feb 25</td>
<td><em>Chapter 9</em></td>
<td>Learning (I)</td>
<td></td>
</tr>
<tr class="odd">
<td>Feb 27</td>
<td><em>Chapter 9</em></td>
<td>Learning (II)</td>
<td></td>
</tr>
<tr class="even">
<th colspan="4" style="font-size: 75%; padding-top: 1em; text-align:left; border-bottom: 1px solid black">WEEK 9</th>
</tr>
<tr class="odd">
<td>Mar 3</td>
<td><em>Chapter 9</em></td>
<td>Learning (III)</td>
<td>#4 posted</td>
</tr>
<tr class="even">
<td>Mar 5</td>
<td><em>Chapter 7</em></td>
<td>Analysing Representations</td>
<td>#3 due (Fri, 6th)*</td>
</tr>
<tr class="odd">
<th colspan="4" style="font-size: 75%; padding-top: 1em; text-align:left; border-bottom: 1px solid black">WEEK 10</th>
</tr>
<tr class="even">
<td>Mar 10</td>
<td><em>provided</em></td>
<td>Symbols (I)</td>
<td></td>
</tr>
<tr class="odd">
<td>Mar 12</td>
<td><em>provided</em></td>
<td>Symbols (II)</td>
<td></td>
</tr>
<tr class="even">
<th colspan="4" style="font-size: 75%; padding-top: 1em; text-align:left; border-bottom: 1px solid black">WEEK 11</th>
</tr>
<tr class="odd">
<td>Mar 17, Mar 19</td>
<td colspan="2"><strong>CLASSES CANCELLED</strong></td>
<td>#4 due* (Tue, 17th)</td>
</tr>
<tr class="odd">
<th colspan="4" style="font-size: 75%; padding-top: 1em; text-align:left; border-bottom: 1px solid black">WEEK 12</th>
</tr>
<tr class="even">
<td>Mar 24</td>
<td><em>provided</em></td>
<td>Action Selection</td>
<td></td>
</tr>
<tr class="odd">
<td>Mar 26</td>
<td><em>provided</em></td>
<td>Spatial Semantic Pointers</td>
<td></td>
</tr>
<tr class="even">
<th colspan="4" style="font-size: 75%; padding-top: 1em; text-align:left; border-bottom: 1px solid black">WEEK 13</th>
</tr>
<tr class="even">
<td>Mar 31</td>
<td><em>provided</em></td>
<td>Biological Details</td>
<td></td>
</tr>
<tr class="odd">
<td>Apr 2</td>
<td></td>
<td>Conclusion</td>
<td></td>
</tr>
<tr class="even">
<th colspan="4" style="font-size: 75%; padding-top: 1em; text-align:left; border-bottom: 1px solid black">WEEK 15</th>
</tr>
<tr class="odd">
<td>Apr 15</td>
<td></td>
<td></td>
<td>Projects due*</td>
</tr>
<tr>
<th colspan="4" style="border-bottom: 3px solid black">
</tr>
</tbody>
</table>

\* The project and all assignments are due at midnight (≈ 11:59p EST) of
that day.

## Grading

The course requires four assignments (60%) and a final project (40%). Assignments are due electronically by  _Midnight_ of the due date. Late assignments lose 1 mark per day and may be at most seven days late. Assignments are to be done individually (everyone writes their own code and answers questions themselves).

## Learning Objectives

By the end of the course students should be able to:

1. **Demonstrate** a basic understanding of neural processes, neural mechanisms, theories of neural communication and computation, and theories of neural dynamics. (KB: 1b, 1c, 1d)
2. **Converse** at a fundamental level with neuroscientists, psychologists, and neural and cogitive modelers. (KB: 1b, I: 3b)
3. **Design** and **Analyze** simple and complex neural circuits for performing small- and large-scale neural computations. (I: 3b, 3c)
4. **Apply** engineering methods in signal processing, optimization, and control theory, among others, to characterizing and building neural circuits. (Kb: 1d, UET: 5c)
5. **Identify** problems and solutions that may exploit the advantages of neural computation in an engineering context. (UET: 5a, 5c)

### Abbreviations
KB - Knowledge base
  - 1b: Demonstrate understanding of concepts in natural science
  - 1c: Demonstrate understanding of engineering fundamentals
  - 1d: Demonstrate understanding of specialized engineering knowledge

I - Investigation
  - 3b: Gather information from relevant sources2 to address complex engineering problems
  - 3c: Synthesize information from multiple sources,such as modeling, simulation or
experiments, to reach valid conclusions

UET - Use of Engineering Tools
  - 5a Select appropriate engineering tools, considering their limitations
  - 5c Use engineering tools appropriately

## Policies

### Academic Integrity

In order to maintain a culture of academic integrity,
members of the University of Waterloo are expected to promote honesty, trust,
fairness, respect and responsibility.

### Discipline

A student is expected to know what constitutes academic
integrity, to avoid committing academic offences, and to take responsibility
for his/her actions. A student who is unsure whether an action constitutes an
offence, or who needs help in learning how to avoid offences (e.g.,
plagiarism, cheating) or about "rules" for group work/collaboration should
seek guidance from the course professor, academic advisor, or the
Undergraduate Associate Dean. When misconduct has been found to have occurred,
disciplinary penalties will be imposed under Policy 71 - Student Discipline.
For information on categories of offenses and types of penalties, students
should refer to [Policy 71 - Student Discipline](http://www.adm.uwaterloo.ca/infosec/Policies/policy71.htm)

### Grievance

A student who believes that a decision affecting some aspect of
his/her university life has been unfair or unreasonable may have grounds for
initiating a grievance. Read [Policy 70 - Student Petitions and Grievances, Section 4](http://www.adm.uwaterloo.ca/infosec/Policies/policy70.htm)

### Appeals

A student may appeal the finding and/or penalty in a decision made
under Policy 70 - Student Petitions and Grievances (other than regarding a
petition) or Policy 71 - Student Discipline if a ground for an appeal can be
established. Read [Policy 72 - Student Appeals](http://www.adm.uwaterloo.ca/infosec/Policies/policy72.htm)

### Academic Integrity Office (UW)

See [http://uwaterloo.ca/academicintegrity/](http://uwaterloo.ca/academicintegrity/)

### Accommodation for Students with Disabilities

The Office for Persons with disabilities (OPD), located in Needles Hall, Room 1132,
collaborates with all academic departments to arrange appropriate accommodations for
students with disabilities without compromising the academic integrity of the curriculum.
If you require academic accommodations to lessen the impact of your disability,
please register with the OPD at the beginning of each academic term.

### Intellectual Property

Students should be aware that this course contains the intellectual property of their instructor, TA, and/or the University of Waterloo.  Intellectual property includes items such as:<ul>
<li>Lecture content, spoken and written (and any audio/video recording thereof);</li>
<li>Lecture handouts, presentations, and other materials prepared for the course (e.g., PowerPoint slides);</li>
<li>Questions or solution sets from various types of assessments (e.g., assignments, quizzes, tests, final exams); and</li>
<li>Work protected by copyright (e.g., any work authored by the instructor or TA or used by the instructor or TA with permission of the copyright owner).</li></ul>

Course materials and the intellectual property contained therein, are used to enhance a student's educational experience.  However, sharing this intellectual property without the intellectual property owner's permission is a violation of intellectual property rights.  For this reason, it is necessary to ask the instructor, TA and/or the University of Waterloo for permission before uploading and sharing the intellectual property of others online (e.g., to an online repository).

Permission from an instructor, TA or the University is also necessary before sharing the intellectual property of others from completed courses with students taking the same/similar courses in subsequent terms/years.  In many cases, instructors might be happy to allow distribution of certain materials.  However, doing so without expressed permission is considered a violation of intellectual property rights.

Please alert the instructor if you become aware of intellectual property belonging to others (past or present) circulating, either through the student body or online.  The intellectual property rights owner deserves to know (and may have already given their consent).
