---
layout: lesson
root: .  # Is the only page that doesn't follow the pattern /:path/index.html
permalink: index.html  # Is the only page that doesn't follow the pattern /:path/index.html
title: An Introduction to the Statistics Tools RooFit, RooStats, and combine
---
> ## Reference Material
> - [Combine Manual](https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit/wiki)
> - [Combine Tutorial at LPC](https://indico.cern.ch/event/747340/timetable/)
> - [Practical Statistics for LHC Physicists](https://indico.cern.ch/event/358542/) - Three CERN Academic Lectures by Harrison Prosper
> - [Statistics in Theory](http://indico.cern.ch/getFile.py/access?contribId=41&sessionId=1&resId=0&materialId=slides&confId=112319) - A lecture by Bob Cousins
> - [RooFit](http://indico.in2p3.fr/materialDisplay.py?contribId=15&materialId=slides&confId=750) - Slides by Wouter Verkerke, one of the [RooFit](https://twiki.cern.ch/twiki/bin/view/CMS/RooFit) developers
> - [RooFit Tutorials](http://root.cern.ch/root/html/tutorials/roofit/index.html) - A set of macros that showcase all major features of RooFit
> - [RooStats Manual](https://twiki.cern.ch/twiki/pub/RooStats/WebHome/RooStats_UsersGuide.pdf) - A concise, clear, summary of statistics concepts and definitions
> - [RooStats Tutorial](http://indico.cern.ch/getFile.py/access?contribId=0&sessionId=1&resId=0&materialId=slides&confId=118720) - Tutorial by Kyle Cranmer, one of the RooStats developers
> - [RooStats Tutorials](http://root.cern.ch/root/html/tutorials/roostats/index.html) - A set of macros that showcase all major features of RooStats
> - [CMS DAS 2014 Statistics Exercise](https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideCMSDataAnalysisSchoolStatistics2014) - A tutorial on statistics as used in CMS
<!-- > - [Advanced uses of combine]() - A tutorial on several advanced features (e.g. signal bias studies, rate parameters, etc.) of combine -->
<!-- > - [CMSDAS-Statistics Github]() - Github repository containing these excercises -->
> - [Procedure for the LHC Higgs boson search combination in Summer 2011](https://cds.cern.ch/record/1379837) - Paper describing LHC statistical procedures
> - [Combine Github](https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit) - Github repository for combine
> - [LPC statistics course](https://indico.cern.ch/event/653271/) - Lectures by Harrison Prosper and Ulrich Heintz, fall 2017
{: .callout}

# Terminology and Conventions
Here we give pragmatic definitions for a few basic concepts that we will use.

- **observable** - something you measure in an experiment, for example, a particle's momentum. Often, a function of measured quantities, for example, an invariant mass of several particles.
- **global observable** or **auxiliary observable** - an observable from another measurement, for example, the integrated luminosity.
- **model** - a set of probability functions (PFs) describing the distributions of observables or functions of observables. The probability functions are called probability density functions (PDFs) if the observables are continuous and probability mass functions (PMF) if the observables are discrete. In the Bayesian approach, the model also includes the prior density.
- **model parameter** - any variable in your model that is not an observable.
- **parameter of interest (POI)** - a model parameter of current interest, for example, a cross section.
- **nuisance parameter** - every model parameter other than your parameter (or parameters) of interest.
- **data** or **data set** - a set of values of observables, either measured in an experiment or simulated.
- **likelihood** - a model computed for a particular data set.
- **hypothesis** - a model in which all quantities are specified: observables, model parameters, and prior PDFs (in case of Bayesian inference).
- **prior** - a probability or probability density for an observable or a model parameter that is independent of the data set. Priors are a key feature of Bayesian inference. However, priors can be used in frequentist inference only if they can be interpreted as relative frequencies.
- **Bayesian** - a school of statistical inference based on the likelihood and a prior.
- **frequentist** - a school of statistical inference based on the likelihood only.

{% include links.md %}