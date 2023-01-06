---
title: "Exercise 4"
math: True
--- 
#  Binned fit to Run I $H→γγ$ data (optional)


We will do a little trick and use the approach known as the so-called "extended likelihood" to define the same model for the counting experiment. This approach naturally extends to a shape analysis. We can write down the corresponding likelihood as


$$ {\cal L} (N|\mu) = \frac{\mu^N e^{-\mu}}{N!} \prod^N_{i=1}\left[\frac{\mu_{SIG}}{\mu} \cdot {\rm Uniform}(x_i) + \frac{\mu_{BG}}{\mu} {\rm Uniform}(x_i) \right] \cdot \mathcal{L}(\mu_{BG})$$


The extended likelihood is misleading name because nothing is extended! If one starts with a multi-bin Poisson likelihood and let the bin size go to zero, one arrives at this likelihood. If on the other hand, one starts with a multinomial likelihood and does the same thing, one finds a similar likelihood as above but without the exponential term outside the product. The use of a likelihood without the exponential presumes that the total event count is fixed.
Here the product is over all events in the dataset. Note that "x" here is a dummy observable, and its values don't matter: you enter your data as the number of events. This likelihood is equivalent to the one in Part 3 (counting experiment).

Now we replace the first Uniform PDF with a Gaussian, and the second Uniform with a background shape like an exponential, and we get the likelihood for a Gaussian-distributed signal over an exponential background.




$$ {\cal L} (\vec{m}|\mu) = \frac{\mu^N e^{-\mu}}{N!} \prod^N_{i=1}\left[\frac{\mu_{SIG}}{\mu} \cdot {\rm Gaussian}(m_i,M,\Gamma) + \frac{\mu_{BG}}{\mu} {\rm Exp}(m_i) \right] \cdot \mathcal{L}(\mu_{BG})$$

This is an often-used kind of model when you measure an invariant mass spectrum and search for a resonance.

Here we fit a model comprising a Gaussian signal on top of a background of the form

$$f_b(x) = \exp[ -(a_1 (x /  100) + a_2 (x / 100)^2) ]$$


> ## Challenge
>  * Change the initial value of the mass. Does the fit always converge to the known solution?
>  * Try a double Gaussian for the signal, with the same mean but differing standard deviations.
>  * Try adding a cubic term to the background model.
{: .challenge}