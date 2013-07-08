title: Addendum

> Neural systems are subject to significant amounts of noise. Therefore, any
analysis of such systems must account for the effects of noise.

There are numerous sources of noise in any physical system, and
neurobiological systems are no exception (see section 2.2.1). As a result, and
despite recent contentions to the contrary (van Gelder and Port 1995), neural
systems can be understood as essentially finite (Eliasmith 2001). This is
important, though not surprising, because it means that information theory is
applicable to analyzing such systems. This ubiquity of noise also suggests
that knowing the limits of neural processing is important for understanding
that processing. For instance, we would not expect neurons to transmit
information at a rate of 10 or 20 bits per spike if the usual sources of noise
limited the signal-to-noise ratio to 10:1, because that would waste valuable
resources. Instead, we would expect information transmission rates of about 3
bits per spike given that signal-to-noise ratio as is found in many
neurobiological systems (see section 4.4.2).

These kinds of limits prove to be very useful for determining how good we can
expect a systems performance to be, and for constraining hypotheses about
what a particular neural system is for. For example, if we choose to model a
system with about 100 neurons (such as the horizontal neural integrator in the
goldfish), and we know that the variance of the noise in the system is about
10%, we can expect a root-mean-squared (RMS) error of about 2% in that
systems representation (see section 2.3). Conversely, we might know the
errors typically observed in a systems behavior and the nature of the
relevant signals, and use this knowledge to guide hypotheses about which
subsystems are involved in which functions. Either way, information regarding
implementational constraints, like noise, can help us learn something new
about the system in which we are interested.
