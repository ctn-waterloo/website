title: "Optimal control of simple arm model: Project status"

### Tasks to do

  * Implement controller for 1-link arm robust to Gaussian white noise in Matlab.
  * Write up derivation of 1-link arm controller robust to Gaussian white noise and load variation.
  * Investigate 'model matching' techniques and applicability to arm control.

###  Progress

**5/8/2009** - Back from week vacation, continuing to read through Athans's paper. The mathematical description of Gaussian white noise has slowed me down, but working through it. Have been reading 'Linear System Theory and Design' as well, have to read more about model matching, where the system is instantly able to track any input signal, and it's applicability/plausibility for an arm control omdel. Recently discovered www.scribd.com, where I downloaded the book. It's a fantastic resource for books and articles. **4/29/2009** - Found paper "The role and use of the stochastic Linear-Quadratic-Gaussian problem in control system design" by Michael Athans (it's linked on my readings page), goes through the reasoning and derivation of a lot of things in detail, and it is very well written and relevant even though it was written in 1971. **4/23/2009** - Implemented simple controller for 1-link arm model in matlab. Handles load variations well, but it's only chance the transfer function deals well with step-input for the reference signal.
