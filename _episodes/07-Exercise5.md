---
math : True
title: Exercise 5
---
# Unbinned fit to Type Ia supernovae distance modulus/red shift data (optional)

This is a fit of the standard model of cosmology to the distance modulus ($μ$) versus redshift ($z$) data from over 500 Type Ia supernovae. Note the use of the C++ function `distanceModulus` to perform a somewhat more elaborate calculation than in the previous exercises. The function `distanceModulus` calculates

$$\mu = 5\ \textrm{log}_{10} \left[ (1 + z)^2 \sin\left( \sqrt{K} d_0\right)/\sqrt{K} \right] + \textrm{ constant},
$$

$$
d_0 = \frac{c}{H_0} \int^1_{(1+z)^{-1}} \frac{da}{a^2 \sqrt{\Omega}}
$$

where K is the curvature constant and d0 is the comoving distance of the supernova (that is, its proper distance at the present epoch). The mass parameter for the standard model of cosmology is given by

$$ \Omega(a) = \frac{\Omega_M}{a^3} +  \frac{(1 - \Omega_M - \Omega_\Lambda)}{a^2} + \Omega_\Lambda.
$$

In the function `LCDMModel` in `distanceModulus.cc`, the value returned is $a^3\Omega(a)$.



> ## Here is a suggested exercise.
>
> Add a function like `LCDMModel` to `distanceModulus` that implements the model
>  
> $$a^3 \Omega(a) = \exp(a^n - 1)$$
> 
> and remember to set the function pointer model to your function in the code snippet > below.
>
> ```
> // pick model
> double (*model)(double, double, double) = LCDMModel;     (change to your function)
> ```
>
> Run the fit with different choices for `n`, say, `n = 0.5, 1.0, 1.5, 2.0, 2.5` and  determine which value gives the best fit to the data.
>
> Something catastrophic happens to this model universe! What?
> 
{: .challenge}



