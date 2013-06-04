title: Comments on Theoretical Neuroscience Books

  1. Rieke, F., D. Warland, R. de Ruyter van Steveninck, and W. Bialek. (1997) _Spikes: Exploring the neural code_. MIT Press.
  2. Wilson, H. R. (1999). _Spikes, decisions, and actions: Dynamical foundations of neuroscience_. Oxford University Press.
  3. Bower, J. M. and D. Beeman (eds.) (1994). _The book of Genesis: Exploring realistic neural models with the GEneral NEural SImulation System_. Springer-Verlag.
  4. Koch, C. (1999). _Biophysics of computation: Information processing in single neurons_. Oxford University Press.
  5. Koch, C. and I. Segev (eds.) (1989). _Methods in neuronal modeling: From synapses to networks_. MIT Press.
  6. Arbib, M. A. (ed.) (1995). _The handbook of brain theory and neural networks_. MIT Press.
  7. Kandel, E. R., J. H. Schwartz, and T. M. Jessell (eds.) (1991). _Principles of neural science_. Third Edition. Elsevier.

## 1.&nbsp_place_holder;&nbsp_place_holder;Spikes: Exploring the neural
code_._

### 1.1&nbsp_place_holder;&nbsp_place_holder;Overview

This book is the ninth in the computational neuroscience series put out by MIT
Press and edited by T. J. Sejnowski and T. A. Poggio. The first book in the
series is the Koch and Segev book we discuss later (section 5). In our view,
it is one of the most important books in this series. This is because it does
an excellent job of laying the foundations for understanding the temporal
nature of the neural code. In particular, Spikes discusses the theory behind
`decoding' the neural code of individual (or more precisely, pairs of)
neurons.

Much of the book is spent analyzing the information transmission
characteristics of individual neurons, with the conclusion that, in general,
neurons are able to transmit between about 2 and 5 bits of information per
neural spike. The book provides fairly detailed coverage of the mathematical
background related to information theory and signals and systems analysis
needed to understand their analysis.

Of less interest to us, another major focus of the book is on issues of
hyperacuity and discriminability.

### 1.2&nbsp_place_holder;&nbsp_place_holder;Strengths and Weaknesses

The greatest strength of this book is that is provides an excellent collection
of empirical results and related theoretical discussions regarding the nature
of coding in individual neurons. These ideas have been previously discussed by
the authors in a number of papers, but nowhere else is the discussion as
complete and thorough. We will be reviewing much of the analysis presented in
this book in the section of the course concerned with temporal coding.

An additional strength is the many mathematical appendices provided for those
wishing to get an in-depth look at the methods, assumptions, and tools used
for generating the results discussed in the main text.

## 2.&nbsp_place_holder;&nbsp_place_holder;Spikes, decisions, and actions:
Dynamical foundations of neuroscience

### 2.1&nbsp_place_holder;&nbsp_place_holder;Overview

Spikes, decisions, and actions is an excellent introduction to low level
single cell modeling. Hugh Wilson provides the necessary mathematical and
neuroscientific background needed to get up to speed on the latest in single
cell modeling. He begins with an insightful discussion of the integrate-and-
fire model, and slowly introduces more and more biophysically realistic
models. However, he doesn't simply focus on biophysical realism. Rather, he
provides, presents and discusses a number of tools for analyzing the behavior
of the models. As well, he discusses means of simplifying extremely complex
models (which are difficult to analyze) in reasonable ways.

A central focus of the book is on nonlinear analysis applied to spiking neural
models. Wilson clearly presents concepts from nonlinear systems theory and
relates them to reduced models of various classes of neurons. This includes a
discussion of bifurcations, limit cycles, chaos, and Lyapunov functions.

Of less interest to us, he also discusses bursting cells, central pattern
generators and other synchrony-related issues currently of interest to many
modelers.

### 2.2&nbsp_place_holder;&nbsp_place_holder;Strengths and Weaknesses

The greatest strength of the book is its clear explanation of all the
necessary concepts, both mathematical and neuroscientific, from nearly first
principles. Anyone rusty in nonlinear systems theory, linear systems theory,
and differential equations will appreciate Wilson's short, but clear
discussion of these issues. As well, he introduces advanced topics in a
concise way.

From our perspective, his discussion of nonlinear neurodynamics and clear
exposition of the methods of reduction from high dimensional single cell
models is most useful. Nowhere else have we found such a good summary of the
literature in this area.

## 3.&nbsp_place_holder;&nbsp_place_holder;The book of Genesis: Exploring
realistic neural models with the GEneral NEural SImulation System

### 3.1&nbsp_place_holder;&nbsp_place_holder;Overview

GENESIS is a well-known, standard neural simulation package available for
free. This book is a collection of chapters that act as tutorials in the use
of the simulation package. Many of the basic modeling techniques used in
computational neuroscience are covered in this book. Topics of the book
include the Hodgkin-Huxley model, compartmental modeling, cable equations,
voltage activated channels as well as topics specific to the simulation
package.

In general, the book is written from the perspective of an experimentalist. A
lot of emphasis is placed on generating models of equal complexity to those
found in real neural systems. So, it is not surprising that much of the book
is spent discussing single cell models, and methods for making them more
realistic. Nevertheless, the simulation tool itself can be used to model
networks of cells as well.

### 3.2&nbsp_place_holder;&nbsp_place_holder;Strengths and Weaknesses

The book provides a an excellent introduction to well-known models in
neuroscience. In particular, the chapters on the Hodgkin-Huxley model,
compartmental modeling and cable equations provide good background, assumed by
many more advanced books in the area. If you plan to do any simulations with
GENESIS (the package), this book is mandatory. If you don't it is still
worthwhile reading many of the earlier chapters that introduce standard
modeling techniques.

From our perspective, this book provides a introduction to the concepts,
vocabulary, and approach used by experimental neuroscientists to modeling
single neuronal cells. This kind of background is very important to have in
order to communicate effectively with more biologically oriented computational
neuroscientists.

## 4.&nbsp_place_holder;&nbsp_place_holder;Biophysics of computation:
Information processing in single neurons

### 4.1&nbsp_place_holder;&nbsp_place_holder;Overview

This book from Christof Koch, a well-respected leader in the field, is a
heroic effort to cover most of the topics in single-cell computational
neuroscience. He provides the basic background on subjects such as cable
theory, membrane equations, the Hodgkin-Huxley model, and passive dendritic
trees, as well as touching on issues of nonlinear systems analysis, voltage-
dependent currents, dendritic spines, active dendrites, and bursting.

For us, this book provides a perspective on the current state of the field in
computational neuroscience. Although our research focusses on the systems
level and this is a book more concerned with single neurons, the Biophysics of
Computation provides a good primer for our research. This is so because these
different levels of explanation and description are mutually dependent. Thus,
we see Koch's book as an invaluable tool for determining what is important to
know about the single neurons that comprise the larger systems that produce
the vast variety of animal behavior.

### 4.2&nbsp_place_holder;&nbsp_place_holder;Strengths and Weaknesses

We have yet to find a book that covers so many different topics of interest to
computational neuroscientists. Unfortunately, many of the discussions are so
short as to be somewhat superficial. However, the numerous citations allow the
reader to pursue topics to great levels of details.

Seldom are so many of the important issues brought together in a single
volume. For those wanting to know what computational neuroscientists are
interested regarding single cells, this book is an unmatched resource.

## 5.&nbsp_place_holder;&nbsp_place_holder;Methods in neuronal modeling: From
synapses to networks

### 5.1&nbsp_place_holder;&nbsp_place_holder;Overview

This book is a classic in computational neuroscience. Even though it was
published decades ago, many of the articles in the collection are cited by
contemporary authors. The papers are generally written by some of the best
known experts in the area. Unlike most of the books we've discussed so far,
this one also has a significant portion of the chapters (3 out of 13)
dedicated to systems level models.

The focus of this book is on the methods used in constructing and simulating
realistic neural models. Thus, there are chapters dedicated to issues of
implementation on parallel computers, numerical methods, and large-scale
simulation construction techniques. Most of the theoretical work is in early
chapters (which focus on the behavior of single neurons). Such subjects as the
cable equations, nonlinear systems analysis, and compartmental modeling are
addressed.

### 5.2&nbsp_place_holder;&nbsp_place_holder;Strengths and Weaknesses

The main strength of this book is that it is a collection of now classic
papers in many of the areas of computational neuroscience. Thus, it provides
good background reading for a number of subjects still central to the
discipline. The main weakness, from our point of view, is the lack of articles
on theoretical analysis of systems level networks.

## 6.&nbsp_place_holder;&nbsp_place_holder;The handbook of brain theory and
neural networks

### 6.1&nbsp_place_holder;&nbsp_place_holder;Overview

This collection of well over 200 articles is a massive tome that provides
unmatched coverage of connectionism, computational neuroscience, and
artificial intelligence. It is something like an encyclopedia of brain theory.
Many articles are written at an introductory level to familiarize the reader
with the relevant issues, and recent insights in the particular field. Because
the focus is on brain _theory_, most articles do not address the relevant
neurobiology in any detail. That being said, there are brief introductions to
neuroanatomy, single cell modeling, neural development, and plasticity.
However, even these sections are more focused on analysis and simulation, than
on facts about the brain.

### 6.2&nbsp_place_holder;&nbsp_place_holder;Strengths and Weaknesses

This collection is simply unmatched in its coverage of theoretical approaches
to brain-like models. Although many of the approaches are somewhat
`unbiological', all are important to understanding the current state of
thought in computational neuroscience. Of course, the book is advertised as
being on brain _theory_, so the downplay of biological facts is precisely what
we should expect. For those facts, we can turn to the final book, below.

## 7.&nbsp_place_holder;&nbsp_place_holder;Principles of neural science

### 7.1&nbsp_place_holder;&nbsp_place_holder;Overview

Simply put, this text is _the_ standard neuroscience textbook. Now in its
sixth edition, the hefty 1200 page volume covers almost all aspects of
neuroscience as it is currently understood. Many of the articles are written
for neuroscience students, and are thus clear and seldom assume much
background in neuroscience. For this reason, it is an ideal resource for those
new to computational neuroscience who are coming from technical fields.

The book discusses major themes of neuroscience, large and small, and includes
in-depth coverage of sensory and motor anatomy and function, the molecular
basis of neuronal behavior and synaptic transmission, neural/behavioral
development, and neural pathologies. If you need to know a neural fact, you
can probably find it here.

### 7.2&nbsp_place_holder;&nbsp_place_holder;Strengths and Weaknesses

The main strength of this volume is its unsurpassed value as a `quick and
easy' source for neuroscientific facts. The main weakness, as we see it, is
that there is seldom any attempt to systematize these facts: this is a
criticism that has been leveled at neuroscience in general by some
theoreticians.
