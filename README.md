# CMS Statistics Data Analsyis School (DAS) Short Exercise

## Introduction

This is a set of tutorials for the CMS Statistics Data Analysis School (DAS) Short Exercise. 

## Main notebooks in this tutorial

 0. [`setup-libraries.ipynb`](setup-libraries.ipynb): setting up libraries using `CMSSW`
 1. [`0/exercise_0.ipynb`](0/exercise_0.ipynb): a very short `PyROOT`/`RooFit` tutorial
 2. [`1/exercise_1.ipynb`](1/exercise_1.ipynb): analyzing a single count using `RooFit`/`RooStats` 
 3. [`2/exercise_2.ipynb`](2/exercise_2.ipynb): analyzing three counts using `RooFit`/`RooStats`
 4. [`3/exercise_3a.ipynb`](3/exercise_3a.ipynb): analyzing three counts using `combine`
 5. [`3/exercise_3b.ipynb`](3/exercise_3b.ipynb): a realistic counting experiment using `combine`
 6. [`3/exercise_3c.ipynb`](3/exercise_3c.ipynb): systematic uncertainties for data-driven background estimates using `combine`
 7. [`4/exercise_4.ipynb`](4/exercise_4.ipynb): binned fit to Run I H->gg data (optional)
 8. [`5/exercise_5.ipynb`](5/exercise_5.ipynb): unbinned fit to Type Ia supernovae distance modulus/red shift data (optional)
 9. [`6/exercise_6.ipynb`](6/exercise_6.ipynb): histogram template analysis using `combine` (optional)
 
## Setup

We will be using the Vanderbilt JupyterHub. 

*Hint! You may want to open this link in a new tab so that you can refer to these instructions for the next steps.*

Point your browser to:

[https://jupyter.accre.vanderbilt.edu/](https://jupyter.accre.vanderbilt.edu/)


If this is the first time using this JupyterHub, you should see:

<p align="center">
  <img src="vanderbilt.png" width="500"/>
</p>

Click the "Sign in with Jupyter ACCRE" button. On the following page, select CERN as your identity provider and click the "Log On" button. Then, enter your CERN credentials or use your CERN grid certificate to autheticate.  

To start a new session, make sure the following drop-down options are selected:
* **Select a Docker image:** *Default ACCRE Image v5*
* **Select a container size:** *1 Core, 2GB RAM, 4 day timeout*

Then click the orange **Spawn** button.

Now you should see the JupyterHub home directory. Click on "New" then "Terminal" in the top right to launch a new terminal.

<p align="center">
  <img src="new_terminal.png" width="200"/>
</p>

To download the tutorials, type

```
git clone https://github.com/FNALLPC/statistics-das
```

*Hint! If you want to cut-and-paste this command in the terminal, highlight the link and copy it as you usually would (Ctrl+c). To paste it, use Shift+Ctrl+v*

Now, in your directory tab, there should be a new directory called `statistics-das`. All of the tutorials and exercises are in there.  Start by clicking on [`setup-libraries.ipynb`](setup-libraries.ipynb) and running it.

## Links

The indico page is: [https://indico.cern.ch/e/cmsdas2020](https://indico.cern.ch/e/cmsdas2020)

The Mattermost for live support is: [https://mattermost.web.cern.ch/cmsdaslpc2019/channels/shortexercisestat](https://mattermost.web.cern.ch/cmsdaslpc2019/channels/shortexercisestat)

The twiki is: [https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolLPC2019StatisticsExercise](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolLPC2019StatisticsExercise)
