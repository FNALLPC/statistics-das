# CMS Data Analysis School (CMSDAS) - Statistics Short Exercise

## Introduction

This is a set of tutorials for the CMS Data Analysis School (CMSDAS) Statistics Short Exercise that are implemented in Jupyter notebooks. The tutorials provide a concise introduction to key ideas in statistics and a few of the statistical analysis tools commonly used in high-energy physics.

## Main notebooks in this tutorial

| __notebooks__   | __description__     |
| :---          | :---        |
| [`setup-libraries.ipynb`](setup-libraries.ipynb) |  setting up libraries using `CMSSW` |
| [`0/exercise_0.ipynb`](0/exercise_0.ipynb) | a very short `PyROOT`/`RooFit` tutorial | 
| [`1/exercise_1.ipynb`](1/exercise_1.ipynb) | analyzing a single count using `RooFit`/`RooStats`  |
| [`2/exercise_2.ipynb`](2/exercise_2.ipynb) | analyzing three counts using `RooFit`/`RooStats` |
| [`3/exercise_3a.ipynb`](3/exercise_3a.ipynb) | analyzing three counts using `combine` | 
| [`3/exercise_3b.ipynb`](3/exercise_3b.ipynb) | a realistic counting experiment using `combine` | 
| [`3/exercise_3c.ipynb`](3/exercise_3c.ipynb) | systematic uncertainties for data-driven background estimates using `combine` |
| [`4/exercise_4.ipynb`](4/exercise_4.ipynb) | binned fit to Run I H->gg data (optional) | 
| [`5/exercise_5.ipynb`](5/exercise_5.ipynb) | unbinned fit to Type Ia supernovae distance modulus/red shift data (optional) |
| [`6/exercise_6.ipynb`](6/exercise_6.ipynb) | histogram template analysis using `combine` (optional) |
 
## Setting up on [Swan](http://swan.web.cern.ch/)

<!-- We will be using the Vanderbilt JupyterHub.

*Hint!* You may want to open this link in a new tab so that you can refer to these instructions for the next steps.

Point your browser to: [https://jupyter.accre.vanderbilt.edu/](https://jupyter.accre.vanderbilt.edu/)

If this is the first time using this JupyterHub, you should see:

![](https://github.com/FNALLPC/statistics-das/raw/master/vanderbilt.png){: width="80%" .image-with-shadow}


Click the "Sign in with Jupyter ACCRE" button. On the following page, select CERN as your identity provider and click the "Log On" button. Then, enter your CERN credentials or use your CERN grid certificate to autheticate.

To start a new session, make sure the following drop-down options are selected:

- Select a Docker image: Default ACCRE Image v5
- Select a container size: 1 Core, 2GB RAM, 4 day timeout

Then click the orange Spawn button. Now you should see the JupyterHub home directory. Click on "New" then "Terminal" in the top right to launch a new terminal.

![](https://github.com/FNALLPC/statistics-das/raw/master/new_terminal.png){: width="29%" .image-with-shadow} -->

1. Go to <http://swan.web.cern.ch/> on your browser

2. Sign in to Single Sign On (SSO) with your CERN account username and password

3. Configure container environment parameters and click on "Start My Session"
> 
> you can use the defauly parameters: (Software Stack: 104a, Platform: CentOS 7 (gcc 11), Number of cores: 4, Memory: 8 GB, Spark cluster: None)
4. On the upper right corner, click on "`New Terminal >_`" button. This opens a new tab with a terminal

5. In the terminal window, download the tutorials by typing:
```bash
git clone https://github.com/FNALLPC/statistics-das
```
6. In the original tab, click on "CERNBox" button at the top

7. There should be a new directory called `statistics-das`. All of the tutorials and exercises are in there. You can directly run one of them by opening them, e.g. `statistics-das/0/exercise_0.ipynb`


## Links

- FNAL github site (instead of twiki) : <https://fnallpc.github.io/statistics-das/>

<!-- The indico page is: [https://indico.cern.ch/e/cmsdas2023](https://indico.cern.ch/e/cmsdas2023) -->

- The Mattermost for live support is: <https://mattermost.web.cern.ch/cmsdaslpc2024/channels/shortex-statistics>. (If you don't have access, see the general CMSDAS instructions for the Mattermost signup link.)

- The twiki is: <https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolLPC2024StatisticsExercise>


