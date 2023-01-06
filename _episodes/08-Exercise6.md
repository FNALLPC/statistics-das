---
math : True
title: Exercise 6
---

# Histogram template analysis using CombinedLimit tool (optional)

In this part of the exercise, we will use the histogram functionality of the 'combine' tool in order to set a limit using one-dimensional non-parametric shapes (i.e. histograms) for a multi-channel analysis (inspired by EXO-11-099).

## Part 6.1 Setting up the input root file
You can get the properly formatted input root file located at `6/shapes_file.root`.

Take a moment to look inside the file. It is especially interesting to look at our observable for signal ("tprime600") and compare with the two backgrounds ("top" and "ewk"). This shape analysis relies on the fact that the signal distribution peaks near zero while the backgrounds peak at high values.

The combine tool looks for the input histograms in a root file formatted according to the pattern you provide in your data card. In this case, we will format the data 
using the following convention:

```
$CHANNEL/$PROCESS_$SYSTEMATIC
```

Our analysis channels in this example are electron+jets ("ejets") and muon+jets ("mujets"). We have a signal process (a t' quark with mass 600 GeV, "tprime600") and two background processes (SM top quark production, "top", and the electroweak backgrounds, "ewk").

We also have two systematic uncertainties which are parameterized by histograms representing a one-sigma shift up and down from the mean, one related to uncertainty in the jet energy scale ("jes") and one for the uncertainty in the b-tagging efficiency scale factor between MC and data ("btgsf").

We will also consider some scaling uncertainties: luminosity (we will assume that the background normalizations are data-driven, so this only affects the signal), background normalization uncertainty for each background (which are assumed to come from our data-driven normalization procedure and can be different for the different backgrounds) and individual uncertainties for electron and muon selection (affecting only the relevant sub-channel). However, since these uncertainties only scale the individual components, we do not need to produce systematic shift histograms for them.

## Part 6.2 Setting up the data card



Now let's create the data card for combine, following the naming scheme used in the file. We will have two analysis channels ("ejets" and "mujets"), two background processes ("top" and "ewk"), and a total of seven systematic uncertainties (enumerated in the previous section). Write down the first block of the data card (you could call it 'myshapes.txt') with the appropriate imax, jmax, and kmax.

> ## Hint
> ```
>imax 2
>jmax 2
>kmax 7
>---------------
>```
{: .solution}



Next, we need a line which tells combine that we are running in shapes mode, and tells it where to find the shapes in our input root file. We do this with the following line:

```
shapes * * shapes_file.root $CHANNEL/$PROCESS  $CHANNEL/$PROCESS_$SYSTEMATIC
---------------
```

Now, we should give our channels the correct names, and specify the number of observed events in each channel (this must match the number of observed events in each channel).


> ## Hint
> ```
>bin ejets mujets
>observation 4734 6448
>---------------
>```
{: .solution}


Next, we need to define the signal and background processes. Let's use process number 1 for top and 2 for ewk. Again, the rate for each process should match the integral of the corresponding histogram. NB that you will need a column for each background in both the ejets and mujets channel!







> ## Hint
> ```
>bin             ejets      ejets   ejets   mujets     mujets    mujets
>process         tprime600  top     ewk     tprime600  top       ewk
>process         0          1       2       0          1         2
>rate            227        4048    760     302        5465.496783      1098.490939
>--------------------------------
>
>```
{: .solution}

Nearing the end, we need to define the systematic uncertainties. Define the following log-normal scaling uncertainties:

- Lumi uncertainty of 10% on the signal in both channels.
- Background normalization uncertainty of 11.4 percent on the top background
- Background normalization uncertainty of 50 percent on the ewk background
- 3 percent uncertainty for electron efficiency
- 3 percent uncertainty for muon efficiency






> ## Hint
> ```
> bin             ejets      ejets   ejets   mujets     mujets    mujets
> process         tprime600  top     ewk     tprime600  top       ewk
> process         0          1       2       0          1         2
> rate            227        4048    760     302        5465.496783      1098.490939
> --------------------------------
> lumi     lnN    1.10        -       -     1.10        -         -
> bgnortop lnN    -          1.114    -     -          1.114      -
> bgnorewk lnN    -           -      1.5    -           -        1.5
> eff_mu   lnN    -           -       -     1.03       1.03      1.03
> eff_e    lnN    1.03       1.03    1.03    -          -         -
>```
{: .solution}



Finally, we need to tell combine about the "jes" and "btgsf" shape uncertainty histograms defined in our input .root file. To do this we use the "shape" type of uncertainty, and give a scaling term for each channel. Here, we'll use "1" for all channels (meaning that the input histogram is meant to represent a 1-sigma shift).

> ## Hint
> The complete card file:
> ```
>imax 2
>jmax 2
>kmax 7
>---------------
>shapes * * shapes_file.root $CHANNEL/$PROCESS  $CHANNEL/$PROCESS_$SYSTEMATIC
>---------------
>bin ejets mujets
>observation 4734 6448
>------------------------------
>bin             ejets      ejets   ejets   mujets     mujets    mujets
>process         tprime600  top     ewk     tprime600  top       ewk
>process         0          1       2       0          1         2
>rate            227        4048    760     302        5465.496783      1098.490939
>--------------------------------
>lumi     lnN    1.10        -       -     1.10        -         -
>bgnortop lnN    -          1.114    -     -          1.114      -
>bgnorewk lnN    -           -      1.5    -           -        1.5
>eff_mu   lnN    -           -       -     1.03       1.03      1.03
>eff_e    lnN    1.03       1.03    1.03    -          -         -
>jes    shape    1           1       1      1          1         1   uncertainty on shape due to JES uncertainty
>btgsf  shape    1           1       1      1          1         1   uncertainty on shape due to b-tagging scale factor uncertainty
> ```
{: .solution}


Now, we can run the tool, using the verbose mode in order to track our histograms being fetched from the input root file:

```
%%bash
combine -v 3 -M AsymptoticLimits  myshapes.txt
```

Take a moment to parse the output of combine. Is the limit you set reasonable given the shapes of the input distributions compared to the data? Given the data, do you expect the limit to be close to the expected limit in the no-signal case?
