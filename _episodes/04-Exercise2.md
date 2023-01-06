---
title: "Exercise 2"
math: True
--- 
# Analyzing three counts using `RooFit/RooStats`

This notebook is a direct generalization of Exercise 1.

This exercise also includes a calculation of the signal significance measure

$$ z = \sqrt{q} $$

where 

$$q(\mu)= -2 \log{\frac{\mathcal{L}_p(\mu)}{\mathcal{L}_p(\hat{\mu})}}$$


defined so that large values of q cast doubt on any hypothesis of the form $μ=μ_0 \not =  \hat{\mu}$, in particular, the background only hypothesis $μ=μ0=0$. The function $\mathcal{L}_p(\mu)$ is the profile likelihood for signal strength $μ$ and $\hat{μ}$ is its maximum likelihood estimate (MLE) (that is, the best fit value)


> ## Mathematical Background 
>> The (profile) likelihood ratio
>>
>> $$ \lambda(\mu) = \frac{\mathcal{L}_p(\mu)}{\mathcal{L}_p(\hat{\mu})} $$
>>  
>>is a useful measure of the compatibility of the observations with the two hypotheses $μ=\mu_0$ and $μ=\hat{\mu}$. Since the latter is the hypothesis that best fits the data, any other hypothesis will have a smaller likelihood. Consequently, $0<λ<1$ with smaller and smaller values indicating greater and greater incompatibility between the given hypothesis about $μ$ and the one that fits the data the best.
>>
>> In order to quantify the degree of incompatibility, the non-Bayesian approach is to compute the probability ${\rm Pr}[λ′<λ(μ)]$. Actually, it is a lot more convenient to work with $q(μ)$ and compute the p-value $p={\rm Pr}[q′>q(μ)]$ because the sampling density of $q(μ)$ can be readily calculated when the observations become sufficiently numerous and, or, the counts become large enough, that is, when we are in the so-called *asymptotic* regime.
>>
>> Define
>>
>> $$ y(\mu) = -2 \log{\mathcal{L}_p(\mu)}$$
>>
>> and consider its expansion about the best fit value
>> 
>> $$ y(\mu)  = y(\hat{\mu} + \mu - \hat{\mu}) = y(\hat{\mu}) +y'(\hat{\mu}) (\mu - \hat{\mu}) + y'' (\hat{\mu})(\mu - \hat{\mu})^2 / 2 + \cdots $$
>> 
>> $$= y(\hat{\mu}) + (\mu - \hat{\mu})^2 / \sigma^2 + \cdots, \quad\quad\sigma^{-2} \equiv y^{''}(\hat{\mu})/2,$$
>>
>> where we have used the fact that the first derivative of $ y$, at the best fit value, is zero provided that the best fit value does not occur on the boundary of the parameter space. (In general, the derivative will not be zero at the boundary.) We have also written the second derivative in terms of a somewhat suggestive symbol! If we can neglect the higher order terms, we can write
>>
>> $$q(\mu) = y(\mu) - y(\hat{\mu}) = (\mu - \hat{\mu})^2 / \sigma^2$$
>>
>>which is called the Wald approximation. If, further, the sampling density of $\hat{\mu}$ can be approximated by the normal density $N(\hat{\mu};\mu',\sigma)$, where, in general, $\mu'$ may differ from $\mu$, then we can derive the density of $z=\sqrt{q}$ by noting that
>>
>> $$\pm z = (\mu - \hat{\mu})/\sigma$$
>>
>>that is, that a given value of $z>0$ corresponds to *two* values of $\hat{\mu}$. With the definitions
>>
>> $$ x= (\hat\mu - \mu')/\sigma$$
>>
>>$$ \delta= (\mu - \mu')/\sigma$$
>>
>> the quantity $x$ assumes two values
>>
>> $$ x = \delta \pm z$$
>>
>> Moreover, $dx = dz$. Therefore, the density of $z$ is given by
>>
>> $$f(z)  =  N(\delta + z; 0, 1) + N(\delta - z; 0, 1)$$
>>
>> $$=  N(z; -\delta, 1) + N(z; \delta, 1),  \quad\quad z > 0 $$
>>
>> from which ${\rm Pr}[z'>z]$ can be calculated for any choice of $\mu$ and $\mu'$, in particular, $\mu=\mu'=0$. In this case, $f(z)=(\chi^2)^{−1/2} f(\chi^2)/2 \ $ reduces to a $\chi^2$ density of one degree of freedom.
{: .solution}

In the Bayesian calculation in this exercise, the marginalization over the nine nuisance parameters is done using Markov Chain Monte Carlo (MCMC), specifically, using the Metropolis-Hastings algorithm. You should see output that looks something like:

 ```
 Floating Parameter    FinalValue +/-  Error   
 --------------------  --------------------------
               b_zx1    7.9495e-01 +/-  1.98e-01
               b_zx2    1.3102e+00 +/-  3.01e-01
               b_zx3    3.9712e-01 +/-  1.97e-01
               b_zz1    1.0987e+00 +/-  9.98e-02
               b_zz2    3.2045e+00 +/-  2.00e-01
               b_zz3    2.4971e+00 +/-  1.99e-01
                  mu    9.0371e-01 +/-  2.95e-01
                  s1    2.9814e+00 +/-  3.94e-01
                  s2    7.9975e+00 +/-  9.87e-01
                  s3    6.3665e+00 +/-  6.88e-01
 
 == Profile likelihood calculations ==
 Info in : file ./fig_PL.png has been created
    68.3% CL interval = [0.628, 1.224]
    95.0% upper limit = 1.458
 mu (MLE)          = 0.904 -0.275/+0.321
 Z = sqrt(q(0))    = 4.164
 where q(mu) = -2*log[Lp(mu)/Lp(mu_hat)]
 
 
 == Bayesian calculations ==
 == using MCMC to perform 9D marginalization integrals
 Metropolis-Hastings progress: ...................................................................................................
 Metropolis-Hastings rogress: ...................................................................................................
 
    68.3% CL interval = [0.432, 1.633]
    95.0% upper limit = 1.481
 ```

> ## Suggested exercises:
> - Repeat the calculation for m_H = 126\textrm{GeV}. You will need to edit the file Table4.dat. 
> 
>> ## Hint
>> You can find the numbers in the table in the Introduction.
>{: .solution}
> - Replace the signal and background likelihoods by Gaussians and re-run.
{: .checklist}

