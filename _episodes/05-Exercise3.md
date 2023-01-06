---
title: "Exercise 3"
math: True
--- 
# HiggsAnalysis / CombinedLimit tool


The [CombinedLimit](https://twiki.cern.ch/twiki/bin/view/CMS/CombinedLimit) tool, which is called `combine`, is a command-line tool, configured with "datacards" - simple human-readable text files, which performs many standard statistical calculations. It's original purpose was to facilitate the combination of results between ATLAS and CMS. The tool makes use of `RooFit` and `RooStats`.

The combine tool should be set up in the first notebook.

## Exercise 3a : Analyzing three counts using HiggsAnalysis / CombinedLimit

Run exercise_3a.ipynb

Can you interpret the results?

> ## Hint
>
> Use
> `combine --help`
> to learn more about the options used above.
{: .solution}



> ## Introduction to Systematic Uncertainties
>>
>> The most common way to introduce systematic uncertainty into a model is via a nuisance parameter and its associated PDF. For example, the uncertainty in the integrated luminosity is estimated to be ~2.6%. We define the size and nature of the variation of the nuisance parameter by multiplying the core model by a PDF that describes the desired uncertainty. There is, however, a subtlety. The PDF of a nuisance parameter is a Bayesian concept! In order to perform a frequentist analysis, we need to get back to the PDF of the *observable* associated with the nuisance parameter; if such exists, we just use its PDF and we're done. If no such observable exists, we use the device of "imagined observables". The PDF of the imagined observable is taken to be directly proportional to the PDF of the nuisance parameter. In other words, we use Bayes theorem: we assume that the PDF of the nuisance parameter is obtained from the PDF of the imagined observable by multiplying the latter by a flat prior for the nuisance parameter. Now that we have extracted the PDF of the imagined observable (or real one if it exists), we merely extend the original model as described above.
>> 
>> The integrated luminosity uncertainty of 2.6% may be accounted for with a Gaussian density with unit mean and a standard deviation of 0.026. With a Gaussian centered at 1 and a standard deviation of 0.026, there is little chance of the Gaussian reaching zero or lower. So, a Gaussian is a fine model for the luminosity uncertainty. However, given that the integrated luminosity cannot be negative, a better model would be one that goes to zero at zero, such as a `log-normal` or `gamma` density. A log-normal density is the probability density of the random variable $y = \kappa^{x} $, when $\kappa$ is a constant and $x$ is a Gaussian random variable.
>>
>>Let's modify our macro to account for the systematic uncertainty in the integrated luminosity. We redefine the `lumi` parameter as a product of its nominal value and a nuisance parameter $\alpha$, which has unit mean and a standard deviation of 0.026:
>>
>> $${\cal{L}} = {\cal{L}}_{NOM} \cdot \alpha_{\cal{L}}$$
>>
>> In principle, we should work through the chain of manipulations that yield the integrated luminosity and construct an accurate likelihood for the data on which the integrated luminosity is based. This likelihood could then be approximated with a simpler function such as a log-normal or gamma density, or even a mixtures of these densities. In practice, (and typically without explicit justification) we almost always use a log-normal model for nuisance parameters. When justification is given, it is typically the following: the product of an arbitrarily large number of independent non-negative random variables follows a log-normal distribution. True. But, this may, or may not, be a relevant result for a given nuisance parameter. Let's however follow convention and define
>>
>> $$ \alpha_{\cal{L}} = \kappa^{\beta} $$
>>
>> Here $\beta$ is a new nuisance parameter that is normally distributed; $\kappa$ is the fractional uncertainty, e.g. for 2.6% uncertainty in the integrated luminosity, $\kappa=1.026$.
{: .solution}

## Exercise 3b: A realistic counting experiment example using the CombinedLimit tool

### Part 3b.1 CombinedLimit : Data card

Create a text file `counting_card.txt` with this content:

```
# Simple counting experiment, with one signal and one background
imax 1  number of channels
jmax 1  number of backgrounds
kmax 0  number of nuisance parameters (sources of systematic uncertainty)
------------
# we have just one channel, in which we observe 0 events
bin 1
observation 0
------------
# now we list the expected events for signal and all backgrounds in that bin
# the second 'process' line must have a positive number for backgrounds, and 0 for signal.
# the line starting with 'rate' gives the expected yield for each process.
# Then (after the '-----'-line), we list the independent sources of uncertainties, and give their effect (syst. error)
# on each process and bin, in this case none.
bin              1     1 
process         sig   bkg
process          0     1 
rate           1.00  0.000001
------------
```

The background-only yield is set to a small value, effectively 0.

### Part 3b.2 CombinedLimit: Run

Let's now run the [CombinedLimit](https://twiki.cern.ch/twiki/bin/view/CMS/CombinedLimit) tool using the model and data defined in the datacard. The program will print out the limit on the signal strength r (mean number of signal events / mean number of predicted signal events). In a notebook cell, try

```
%%bash
combine -M AsymptoticLimits counting_card.txt
```

You just computed an Asymptotic frequentist 95% one-sided confidence interval (upper limit) for the signal yield. We will discuss available options, their defaults and details of this calculation in another section. Try the same computation using toys instead of the asymptotic formulae.

```
%%bash 
combine -M HybridNew --frequentist --testStat LHC -H AsymptoticLimits counting_card.txt
```

Do you get a different answer? If so, why?

### Part 3b.3 CombinedLimit: Accounting for Systematic Uncertainties

It is rather straightforward to add systematic uncertainties to a CombinedLimit data card, including correlated ones. Let's use the counting experiment model that we created, and account for systematic uncertainty in

- the integrated luminosity (5%, which affects both signal and background in a correlated way),
- the signal efficiency and acceptance (10%),
- the background rate (20%).

Now your card file looks like this. Note the last three lines, and a change in number of the nuisance parameters at the top:

```
# Simple counting experiment, with one signal and one background
imax 1  number of channels
jmax 1  number of backgrounds
kmax 3  number of nuisance parameters (sources of systematic uncertainty)
------------
# we have just one channel, in which we observe 0 events
bin 1
observation 0
------------
# now we list the expected number of events for signal and all backgrounds in that bin
# the second 'process' line must have a positive number for backgrounds, and 0 for signal
# then we list the independent sources of uncertainties, and give their effect (syst. error)
# on each process and bin
bin              1     1 
process         sig   bkg
process          0     1 
rate           1.00  0.000001
------------
lumi     lnN    1.05  1.05   lumi affects both signal and background (mc-driven). lnN = lognormal
xs_sig   lnN    1.10    -    signal efficiency x acceptance (10%)
bkg_norm lnN      -   1.20   background rate (=> 20% statistical uncertainty)
```

Now you can try the calculation again:

```
%%bash
combine -M AsymptoticLimits counting_card.txt
```



> ## Note
> the result - the limit - has not changed much. This is actually an interesting and convenient feature: it has been noted that, in the absence of signal, the systematic uncertainty in the model parameters usually only slightly affect the limit on the signal yield (Cousins and Highland). i.e., ~10% uncertainty in the background yield is expected to change the limit by ~1% or less compared to the case without systematic uncertainties.
{: .callout}


## Exercise 3c: Systematic uncertainties for data-driven background estimates

Let's get back to discussing the systematic uncertainties. In one of the previous sections, we defined so-called "[Lognormal](http://en.wikipedia.org/wiki/Log-normal_distribution)" model for systematic uncertainties (hence `lnN` in the datacard). The Lognormal model is appropriate in most cases, and is recommended instead of the Gaussian model unless, of course, the quantities can be negative in which case the log-normal and gamma models would be inappropriate. A Gaussian is inappropriate for a parameter that is bounded, such as an efficiency, an integrated luminosity, or a background, none of which can be negative. The Lognormal model is also well-suited to model very large uncertainties, >100%. Moreover, away from the boundary, the Lognormal shape is very similar to a Gaussian one. Nevertheless, if the uncertainties are large, it would be wise to check whether a log-normal or a gamma is adequate. If they are not, it may be necessary to model the systematic uncertainties more explicitly.


A "[Gamma](http://en.wikipedia.org/wiki/Gamma_distribution)" model is often more suitable for modeling systematic uncertainty associated with a signal yield. This is a common case, when you have a background rate estimate, with uncertainty, as in the example in your data card. 
The reason for the Gamma is straightforward: the background rate $(N_{bg})$ is distributed according to a ${\rm Poisson}(N_{bg} |  \mu_{BG})$, so the mean used in your model $(\mu_{BG})$ as the predicted rate is (from a Bayesian perspective) distributed as a $\Gamma(\mu_{BG} | N_{bg} + 1)$ if one assumes a flat prior for the background mean $\mu_{BG}$. (Note that $N_{bg}$ here is what we call a "global observable" - that is, the outcome of an auxiliary experiment that yielded the background estimate.)

Let's create a new data card, which is more realistic and taken from the CombinedLimit manual. It describes a $H \to WW$ counting experiment. It is included in the repository and called `realistic_counting_experiment.txt`:


```
# Simple counting experiment, with one signal and a few background processes
# Simplified version of the 35/pb H->WW analysis for mH = 160 GeV
imax 1  number of channels
jmax 3  number of backgrounds
kmax 5  number of nuisance parameters (sources of systematical uncertainties)
------------
# we have just one channel, in which we observe 0 events
bin 1
observation 0
------------
# now we list the expected events for signal and all backgrounds in that bin
# the second 'process' line must have a positive number for backgrounds, and 0 for signal
# then we list the independent sources of uncertainties, and give their effect (syst. error)
# on each process and bin
bin              1     1     1     1
process         ggH  qqWW  ggWW  others
process          0     1     2     3
rate           1.47  0.63  0.06  0.22
------------
lumi    lnN    1.11    -   1.11    -    lumi affects both signal and gg->WW (mc-driven). lnN = lognormal
xs_ggH  lnN    1.16    -     -     -    gg->H cross section + signal efficiency + other minor ones.
WW_norm gmN 4    -   0.16    -     -    WW estimate of 0.64 comes from sidebands: 4 events in sideband times 0.16 (=> ~50% statistical uncertainty)
xs_ggWW lnN      -     -   1.50    -    50% uncertainty on gg->WW cross section
bg_others lnN    -     -     -   1.30   30% uncertainty on the rest of the backgrounds
```



Note that the WW background is data-driven: it is estimated from a background-dominated control region in experimental data. In this case, 4 events were observed in this control region, and it is estimated, that the scale factor to the signal region is 0.16. It means that for each event in the control sample, we expect a mean of 0.16 events in the signal region.

Here's a more detailed description of the systematics part of the data card from the CombinedLimit manual:
```
lumi    lnN    1.11    -   1.11    -    lumi affects both signal and gg->WW (mc-driven). lnN = lognormal
xs_ggH  lnN    1.16    -     -     -    gg->H cross section + signal efficiency + other minor ones.
WW_norm gmN 4    -   0.16    -     -    WW estimate of 0.64 comes from sidebands: 4 events in sideband times 0.16 (=> ~50% statistical uncertainty)
xs_ggWW lnN      -     -   1.50    -    50% uncertainty on gg->WW cross section
bg_others lnN    -     -     -   1.30   30% uncertainty on the rest of the backgrounds
```



- the first columns is a label identifying the uncertainty
- the second column identifies the type of distribution used
  - `lnN` stands for Log-normal, which is the recommended choice for multiplicative corrections (efficiencies, cross sections, ...).
If $\Delta x/x$ is the relative uncertainty on the multiplicative correction, one should put $1+\Delta x/x$ in the column corresponding to the process and channel
  - `gmN` stands for Gamma, and is the recommended choice for the statistical uncertainty on a background coming from the number of events in a control region (or in a MC sample with limited statistics).
If the control region or MC contains $N$ events, and the extrapolation factor from the control region to the signal region is $α$ then one shoud put $N$ just after the `gmN` keyword, and then the value of $α$ in the proper column. Also, the yield in the `rate` row should match with $N\times α$
- then there are (#channels)$\times$(#processes) columns reporting the relative effect of the systematic uncertainty on the rate of each process in each channel. The columns are aligned with the ones in the previous lines declaring bins, processes and rates.


In the example, there are 5 uncertainties:

- the first uncertainty affects the signal by 11%, and affects the `ggWW` process by 11%
- the second uncertainty affects the signal by 16% leaving the backgrounds unaffected
- the third line specifies that the `qqWW` background comes from a sideband with 4 observed events and an extrapolation factor of 0.16; the resulting uncertainty on the expected yield is $1/\sqrt{(4+1)} = 45\%$
- the fourth uncertainty does not affect the signal, affects the `ggWW`= background by 50%, leaving the other backgrounds unaffected
- the last uncertainty does not affect the signal, affects by 30% the `others` backgrounds, leaving the rest of the backgrounds unaffected

> ## Exercise 
>  Run the CombinedLimit tool for the Higgs to WW data card above and compute an Asymptotic upper limit on the signal cross section ratio $σ/σ_{SM}$.
{: .challenge}

### Part 3c.1 CombinedLimit: CLs, Bayesian and Feldman-Cousins


Now that we reviewed aspects of model building, let's get acquainted with available ways to estimate confidence and credible intervals, including upper limits. (Note that, even though we use "confidence" and "credible" interval nomenclatures interchangeably, the proper nomenclature is "confidence interval" for a frequentist calculation, and "credible interval" for Bayesian. Of course, none of the methods, which we use in CMS, are purely one or the other, but that's a separate sad story for another day.)

For the advantages and differences between the different methods, we refer you to external material: especially look through the lecture by Robert Cousins, it is linked in the References section.

Practically, the current policy in CMS prescribes to use "frequentist" version of the CLs for upper limit estimates, either "full" or "asymptotic". Use of Bayesian upper limit estimates is permitted on a case-by-case basis, usually in extremely difficult cases for CLs, or where there is a long tradition of publishing Bayesian limits. **Note** that CLs can only be used for limits, and not for central intervals, so it is unsuitable for discovery. For central intervals, there is no clear recommendation yet but the Feldman-Cousins and Bayesian estimates are encouraged. Finally, it is very advisable to remember the applicability of each method and cross check using alternative methods when possible.

Note that you can run the limit calculations in the same way for any model that you managed to define in a data card. This is an important point: in our approach, the model building and the statistical estimate are independent procedures! We will use the "realistic" data card as an example, and run several limit calculations for it, using the CombinedLimit tool. You can do the same calculation for any other model in the same way.

### Part 3c.2 CombinedLimit: Asymptotic CLs Limit

*This section on asymptotic CLs calculation is taken in part from the CombinedLimit manual by Giovanni Petrucciani.*

The asymptotic CLS method allows to compute quickly an estimate of the observed and expected limits, which is fairly accurate when the event yields are not too small and the systematic uncertainties don't play a major role in the result. Just do


```
combine -M Asymptotic realistic_counting_experiment.txt
```
The program will print out the limit on the signal strength r (number of signal events / number of expected signal events) e .g. `Observed Limit: r < 1.6297 @ 95% CL` , the median expected limit `Expected 50.0%: r < 2.3111` and edges of the 68% and 95% ranges for the expected limits.

> ## Asymptotic limit output
>> ```
>> >>> including systematics
>> >>> method used to compute upper limit is Asymptotic
>> [...]
>> -- Asymptotic -- 
>> Observed Limit: r < 1.6297
>> Expected  2.5%: r < 1.2539
>> Expected 16.0%: r < 1.6679
>> Expected 50.0%: r < 2.3111
>> Expected 84.0%: r < 3.2102
>> Expected 97.5%: r < 4.2651
>> 
>> Done in 0.01 min (cpu), 0.01 min (real)
>> ``` 
>> {: .output}
{: .solution}


The program will also create a rootfile `higgsCombineTest.Asymptotic.mH120.root` containing a root tree `limit` that contains the limit values and other bookeeping information. The important columns are `limit` (the limit value) and `quantileExpected` (-1 for observed limit, 0.5 for median expected limit, 0.16/0.84 for the edges of the $±1σ$ band of expected limits, 0.025/0.975 for $±2σ$).


> ## Show tree contents
>> ```
>> $ root -l higgsCombineTest.Asymptotic.mH120.root 
root [0] limit->Scan("*")
************************************************************************************************************************************
*    Row   *     limit *  limitErr *        mh *      syst *      iToy *     iSeed *  iChannel *     t_cpu *    t_real * quantileExpected *
************************************************************************************************************************************
*        0 * 1.2539002 *         0 *       120 *         1 *         0 *    123456 *         0 *         0 *         0 * 0.0250000 *
*        1 * 1.6678826 *         0 *       120 *         1 *         0 *    123456 *         0 *         0 *         0 * 0.1599999 *
*        2 * 2.3111260 *         0 *       120 *         1 *         0 *    123456 *         0 *         0 *         0 *       0.5 *  ← median expected limit
*        3 * 3.2101566 *         0 *       120 *         1 *         0 *    123456 *         0 *         0 *         0 * 0.8399999 *
*        4 * 4.2651203 *         0 *       120 *         1 *         0 *    123456 *         0 *         0 *         0 * 0.9750000 *
*        5 * 1.6296688 * 0.0077974 *       120 *         1 *         0 *    123456 *         0 * 0.0049999 * 0.0050977 *        -1 * ← observed limit
************************************************************************************************************************************
>> ``` 
>> {: .output}
{: .solution}


A few command line options of `combine` can be used to control this output:

- The option `-n` allows you to specify part of the name of the rootfile. e.g. if you do `-n HWW` the roofile will be called `higgsCombineHWW....` instead of `higgsCombineTest`
- The option `-m` allows you to specify the higgs boson mass, which gets written in the filename and also in the tree (this simplifies the bookeeping because you can merge together multiple trees corresponding to different higgs masses using `hadd` and then use the tree to plot the value of the limit vs mass) (default is m=120)


There are some common configurables that apply to all methods:

- `H`: run first another faster algorithm (e.g. the AsymptoticLimits described below) to get a hint of the limit, allowing the real algorithm to converge more quickly. We **strongly recommend** to use this option when using MarkovChainMC, HybridNew, Hybrid or FeldmanCousins calculators, unless you know in which range your limit lies and you set it manually (the default is `[0, 20]`)
- `rMax`, `rMin`: manually restrict the range of signal strengths to consider. For Bayesian limits with MCMC, `rMax` a rule of thumb is that `rMax` should be 3-5 times the limit (a too small value of `rMax` will bias your limit towards low values, since you are restricting the integration range, while a too large value will bias you to higher limits)
- `freezeParameters`: if set to "allConstrainedNuisances", any **systematic uncertainties** (i.e. nuisance parameters that have an explicit constraint term) are frozen and only statistical uncertainties are considered. See [https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/runningthetool/#common-command-line-options](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/runningthetool/#common-command-line-options) for additional common options and further explanations



Most methods have multiple configuration options; you can get a list of all them by invoking `combine --help`

> ## Exercise
> Run the CombinedLimit tool with extra options described in this section. Try `combine --help` and see at the options for the AsymptoticLimits there. Try some options.
{: .challenge}

### Part 3c.3 CombinedLimit: full frequentist CLs limit
*This section on asymptotic CLs calculation is taken in part from the CombinedLimit manual by Giovanni Petrucciani.*

The HybridNew method is used to compute either the hybrid bayesian-frequentist limits popularly known as "CLs of LEP or Tevatron type" or the fully frequentist limits which are the current recommended method by the LHC Higgs Combination Group. Note that these methods can be resource intensive for complex models.

Example frequentist limit (note: it takes ~20 minutes to run)

```
%%bash
combine -M HybridNew --frequentist --testStat LHC realistic_counting_experiment.txt 
```

> ## Hybrid limit output
>> 
>> ```
>> including systematics
>> using the Profile Likelihood test statistics modified for upper limits (Q_LHC)
>> method used to compute upper limit is HybridNew
>> method used to hint where the upper limit is ProfileLikelihood
>> random number generator seed is 123456
>>loaded
>>Computing limit starting from observation
>>
>> -- Profile Likelihood -- 
>>Limit: r < 1.3488 @ 95% CL
>>Search for upper limit to the limit
>>  r = 4.04641 +/- 0
>>   CLs = 0 +/- 0
>>   CLs      = 0 +/- 0
>>   CLb      = 0.209677 +/- 0.0365567
>>   CLsplusb = 0 +/- 0
>>
>>Search for lower limit to the limit
>>  r = 0.404641 +/- 0
>>   CLs = 0.529067 +/- 0.10434
>>   CLs      = 0.529067 +/- 0.10434
>>   CLb      = 0.241935 +/- 0.0384585
>>   CLsplusb = 0.128 +/- 0.014941
>>
>>Now doing proper bracketing & bisection
>>  r = 2.22553 +/- 1.82088
>>   CLs = 0.0145882 +/- 0.0105131
>>   CLs      = 0.0145882 +/- 0.0105131
>>   CLb      = 0.274194 +/- 0.0400616
>>   CLsplusb = 0.004 +/- 0.00282276
>>
>>  r = 1.6009 +/- 0.364177
>>   CLs = 0.088 +/- 0.029595
>>   CLs = 0.076 +/- 0.0191569
>>   CLs = 0.0863004 +/- 0.017249
>>   CLs = 0.0719667 +/- 0.0135168
>>   CLs = 0.0731836 +/- 0.0123952
>>   CLs = 0.074031 +/- 0.0115098
>>   CLs = 0.0795652 +/- 0.010995
>>   CLs = 0.0782988 +/- 0.0100371
>>   CLs = 0.0759706 +/- 0.00928236
>>   CLs = 0.073037 +/- 0.00868742
>>   CLs = 0.0723792 +/- 0.00822305
>>   CLs = 0.0720354 +/- 0.00784983
>>   CLs = 0.0717446 +/- 0.00752306
>>   CLs = 0.0692283 +/- 0.00701054
>>   CLs = 0.0684187 +/- 0.00669284
>>   CLs = 0.0683436 +/- 0.00653234
>>   CLs = 0.0673759 +/- 0.00631413
>>   CLs = 0.0683407 +/- 0.00625591
>>   CLs = 0.0696201 +/- 0.0061699
>>   CLs      = 0.0696201 +/- 0.0061699
>>   CLb      = 0.229819 +/- 0.00853817
>>   CLsplusb = 0.016 +/- 0.00128735
>>
>>  r = 1.7332 +/- 0.124926
>>   CLs = 0.118609 +/- 0.0418208
>>   CLs = 0.108 +/- 0.0271205
>>   CLs = 0.0844444 +/- 0.0181279
>>   CLs = 0.07874 +/- 0.0157065
>>   CLs = 0.0777917 +/- 0.0141997
>>   CLs = 0.0734944 +/- 0.0123691
>>   CLs = 0.075729 +/- 0.0116185
>>   CLs = 0.0711058 +/- 0.0102596
>>   CLs = 0.0703755 +/- 0.00966018
>>   CLs = 0.068973 +/- 0.00903599
>>   CLs = 0.0715126 +/- 0.00884858
>>   CLs = 0.0691189 +/- 0.00821614
>>   CLs = 0.0717797 +/- 0.00809828
>>   CLs = 0.0726772 +/- 0.0078844
>>   CLs = 0.073743 +/- 0.00768154
>>   CLs      = 0.073743 +/- 0.00768154
>>   CLb      = 0.202505 +/- 0.00918088
>>   CLsplusb = 0.0149333 +/- 0.00140049
>> 
>>
>> -- Hybrid New -- 
>>Limit: r < 1.85126 +/- 0.0984649 @ 95% CL
>>Done in 0.00 min (cpu), 0.55 min (real)
>> ```
>> {: .output}
>>
{: .solution} 

> ## HybridNew parameters
> More information about the HybridNew parameters is available in [HybridNew](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolLPC2023StatisticsExercise#HybridNew) algorithm section in the manual. Instructions on how to use the HybridNew for complex models where running the limit in a single job is not practical are also provided in the section [HybridNew algorithm and grids](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolLPC2023StatisticsExercise#HybridNewGrid).
{: .callout}

> ## Note 
> The possible confusion: the name of the method in the tool "HybridNew" is historical and implies a hybrid frequentist-Bayesian calculation, where the systematic uncertainties are treated in a Bayesian way. This is not what we do in this section, despite the name of the method. We do a "fully frequentist" treatment of the systematic uncertainties (hence the --`frequentist` modifier).
{: .callout}



### Part 3c.4 CombinedLimit: Computing Feldman-Cousins bands

*This section on asymptotic CLs calculation is taken in part from the [CombinedLimit](https://twiki.cern.ch/twiki/bin/view/CMS/CombinedLimit) manual by Giovanni Petrucciani.*


> ## ALERT! 
> Since this is not one of the default statistical methods used within the Higgs  group, this method has not been tested rigorously.
{: .caution}


Uses the F-C procedure to compute a confidence interval which could be either 1 sided or 2 sided. When systematics are included, the profiled likelihood is used to define the ordering rule.

```
%%bash
combine -M FeldmanCousins  realistic_counting_experiment.txt 
```

> ## Feldman-Cousins limit output 
> ```
> >>> including systematics
> >>> method used to compute upper limit is FeldmanCousins
> >>> random number generator seed is 123456
> loaded
> Computing limit starting from observation
>   would be r < 4 +/- 1
>   would be r < 1.6 +/- 0.3
>   would be r < 1.45 +/- 0.075
>
> -- FeldmanCousins++ -- 
>Limit: r< 1.45 +/- 0.075 @ 95% CL
>Done in 0.12 min (cpu), 0.12 min (real)
>```
> {: .output}
{: .solution}


To compute the lower limit instead of the upper limit specify the option `--lowerLimit`:

```
%%bash
combine -M FeldmanCousins --lowerLimit realistic_counting_experiment.txt 
```
> ## Feldman-Cousins limit output 
> ```
> -- FeldmanCousins++ -- 
>Limit: r> 0.05 +/- 0.05 @ 95% CL
> ```
{: .solution}

### Part 3c.5 CombinedLimit: Compute the observed significance


*This section on asymptotic CLs calculation is taken from the CombinedLimit manual by Giovanni Petrucciani.*

Just use the Significance method and the program will compute the significance instead of the limit.

```
%%bash
combine -M Significance realistic_counting_experiment.txt
```

You can also compute the significance with the HybridNew method. For the hybrid methods, there is no adaptive MC generation so you need to specify the number of toys to run (option `-T`), and you might want to split this computation in multiple jobs (instructions are below in the HybridNew section).

```
%%bash
combine -M HybridNew --signif realistic_counting_experiment.txt
```

If you want to play with this method, you can edit `realistic_counting_experiment.txt` and change the number of observed events 3 (to get some non-zero significance), and execute

```
%%bash
combine -M Significance realistic_counting_experiment.txt
```



