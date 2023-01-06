---
title: "Exercise 0"
math: True
--- 
# A very short `Python/PyROOT/RooFit` tutorial

> ## Mathematical Background 
>> The notebook `exercise_0.ipynb` generates data from the model
>> 
>> $$f(x;\theta)=a\exp(-x/b)/b+(1-a)\exp(-x/c)/c,\quad\theta=a,b,c$$
>> 
>> $$\int f(x;\theta)\; dx=1$$
>> 
>> and fits the data to the same model using both un-binned and binned fits. In both cases, `Minuit` is used to minimize the negative log-likelihood,
>>
>> $$ l(\theta) = - \ln \mathcal{L}(\theta) $$
>>
>> with respect to the parameters $\theta$ of the model. For the un-binned fit, the *likelihood* (that is, the pdf evaluated at the observed data) is
>> 
>> $$ \mathcal{L}(\theta) = \prod_{i=1}^T f(x_i; \theta) $$
>>
>> where $T$ is the number of data. For the binned fit, the likelihood is the multinomial
>>
>> $$\mathcal{L}(\theta) = \prod_{i=1}^M p_i^{N_i}$$
>>
>> where $M$ is the number of bins, $N_i$ the count in the $i^{\text{th}}$ bin,
>>
>> $$ p_i = \frac{n_i}{\sum_{j=1}^M n_j} $$
>>
>> and the expected count in the $i^{\text{th}}$ bin is
>>
>> $$n_i = T \int_{\text{bin}_i} f(x;\theta)\; dx$$
>>
>> ### Quality of binned fit
>> The quality of the binned fit is assessed using two *goodness-of-fit* (gof) measures
>>
>> $$X = \sum_{i=1}^M \frac{(N_i - n_i)^2}{n_i}$$
>>
>> and
>>
>> $$Y = -2 \sum_{i=1}^M N_i \ln (n_i / N_i) $$ 
>>
>> According to Wilks theorem (1938), if the hypothesis $H_0 : \theta= \theta_0$  is true, and $\theta_0$ does not lie on the boundary of the parameter space (plus some other mild conditions), then *asymptotically* (that is, as $T\to \infty$) both measures have a $\chi^2_K$ distribution of $K$ degrees of freedom. For a multinomial distribution with $M$ bins and $P$ fitted parameters $K=M−1−P$. The true hypothesis $H_0$ is approximated by setting $\theta_0=\hat{\theta}$, the best fit values (that is, *maximum likelihood estimates* (MLE)) of $\theta$.
>> 
>> If $X \approx Y \approx K$, we may conclude that we have no grounds for rejecting the hypothesis $H_0$. A probabilistic way to say the same thing is to compute a *p-value*, defined by
>>
>> $$ \text{p-value} = \rm{Pr}(X' > X | H_0), $$
>>
>> under the assumption that $H_0$ is true and *reject* the hypothesis if the p-value is judged to be too small. The intuition here is that if we observe a gof measure that is way off in the tail of the distribution of $X$, then either a rare fluctuation has occurred or the hypothesis $H_0$ is false. It is a matter of judgment and, or, convention which conclusion is to be adopted.
>>
>> All of this, of course, depends on the validity of the asymptotic approximation. One way to check whether the approximation is reasonable is to compare the measures $X$ and $Y$, or, equivalently, their associated p-values. Should they turn out to be about the same, then we can happily conclude that the land of *Asymptotia* is in sight!
{: .solution}

In this exercise you will learn how to use `RooFit` (via the `Python/ROOT` interface, `PyROOT`) to fit functions to data. As an example, the notebook `exercise_0.ipynb` generates "pseudo-data" from a given model, and then fits that pseudo-data using the same functional form. The first part of the exercise consists simply of running the notebook `exercise_0.ipynb`, reading through the program, and trying to understand what it is doing.

This program fits a double exponential to the unbinned pseudo-data. The pseudo-data are then binned and a binned fit is performed using a multinomial likelihood. Finally, two goodness-of-fit (*gof*) measures are calculated and converted into p-values. (See mathematical background for details.) The last output you should see should look something like


```
Info in : file ./fig_binnedFit.png has been created
================================================================================

            binlow count       mean
    1        0.000   109      103.4
    2        1.333    70       71.1
    3        2.667    48       50.6
    4        4.000    33       37.2
    5        5.333    33       28.3
    6        6.667    18       22.2
    7        8.000    16       17.8
    8        9.333    16       14.6
    9       10.667    17       12.1
   10       12.000     8       10.2
   11       13.333     8        8.7
   12       14.667     9        7.4
   13       16.000     5        6.3
   14       17.333     6        5.4
   15       18.667     4        4.7
================================================================================
Int p(x|xi) dx = 400.0

ChiSq/ndf =    6.0/10 (using X)
p-value   =    0.8153

ChiSq/ndf =    7.2/10 (using Y)
p-value   =    0.7033
```
{: .output}

and two plots should appear, then disappear. Read through the notebook `exercise_0.ipynb` and try to understand what it is doing. Feel free to play around with the notebook. 

> ## Suggestions
> - [x] Change the number of pseudo-data events to generate and re-run the fit.
> - [x] Change the number of bins and re-run the fit.
> - [x] Add a new function (for example, a Gaussian + an exponential) to models.cc, modify the notebook to use it by modifying the code highlighted below, and re-run. 
{: .checklist}

```python
gROOT.ProcessLine(open('models.cc').read())
from ROOT import dbexp
wspace.factory('GenericPdf::model("dbexp(x,a,b,c)", {x,a,b,c})')
```
If you add more parameters, you'll need to modify the code block:

```python
# The parameters of the model are a, b, c
wspace.factory('a[0.4, 0.0,   1.0]')
wspace.factory('b[3.0, 0.01, 20.0]')
wspace.factory('c[9.0, 0.01, 20.0]')
parameters = ['a', 'b', 'c']

# NUMBER OF PARAMETERS
P = len(parameters)
```