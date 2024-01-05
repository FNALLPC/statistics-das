# CMS Data Analysis School (CMSDAS): Statistics Short Exercise

## Introduction

This is a set of tutorials for the CMS Data Analysis School (CMSDAS) Statistics Short Exercise that are implemented in Jupyter notebooks. The tutorials provide a concise introduction to key ideas in statistics and a few of the statistical analysis tools commonly used in high-energy physics.

## Notebooks

| __notebooks__   | __description__     |
| :---          | :---        |
| [`0/exercise_0.ipynb`](0/exercise_0.ipynb) | a very short `PyROOT`/`RooFit` tutorial | 
| [`1/exercise_1.ipynb`](1/exercise_1.ipynb) | analyzing a single count using `RooFit`/`RooStats`  |
| [`2/exercise_2.ipynb`](2/exercise_2.ipynb) | analyzing three counts using `RooFit`/`RooStats` |
| [`3/exercise_3a.ipynb`](3/exercise_3a.ipynb) | analyzing three counts using `combine` | 
| [`3/exercise_3b.ipynb`](3/exercise_3b.ipynb) | a realistic counting experiment using `combine` | 
| [`3/exercise_3c.ipynb`](3/exercise_3c.ipynb) | systematic uncertainties for data-driven background estimates using `combine` |
| [`4/exercise_4.ipynb`](4/exercise_4.ipynb) | binned fit to Run I H->gg data (optional) | 
| [`5/exercise_5.ipynb`](5/exercise_5.ipynb) | unbinned fit to Type Ia supernovae distance modulus/red shift data (optional) |
| [`6/exercise_6.ipynb`](6/exercise_6.ipynb) | histogram template analysis using `combine` (optional) |
 
## Getting Started on [Swan](http://swan.web.cern.ch/)

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

1. Go to <http://swan.web.cern.ch/> with your browser.

2. Sign on to your CERN account username and password using Single Sign On (SSO). 

3. Under `Configure Environment`, click the `Start my Session` button. 
> 
> you can use the default parameters: Software Stack: 104a, Platform: CentOS 7 (gcc 11), Number of cores: 4, Memory: 8 GB, Spark cluster: None
4. In the upper right corner, click on the New Terminal button `>_` to open a terminal window in a new tab in your browser. Go to the new tab and type `ls`, then return (or enter) in the terminal window. You will see a list of the files in your CERNBox home directory. You may also see a directory (i.e., folder) called `SWAN_projects`. If one does not exist, create one using:
```bash
mkdir SWAN_projects
```

5. In the terminal window, navigate to `SWAN_projects` and download the tutorials by typing:
```bash
cd
cd SWAN_projects
git clone https://github.com/FNALLPC/statistics-das.git
```
6. In the original tab, click on the `CERNBox` button at the top of the page and click on the folder `SWAN_projects`. There should be a new directory called `statistics-das`. All of the tutorials and exercises are in there.
7. To open a notebook, e.g. `statistics-das/0/exercise_0.ipynb`, simply click on the file.

## Notebook Tips
Jupyter notebooks are structured into **cells**. It is recommended that you execute the notebooks one cell at a time to ensure that each cell works as expected. And, yes, cells should be executed sequentially! Of course, if you're careful, you can go back and re-execute cells. But remember jupyter notebooks are ``sticky'' in that the notebook pays attention to the order in which cells have been executed. This can lead to confusion. If things get really messed up, it's usually better to re-launch the jupyter kernel and start again from scratch.

### Some useful shortcuts
- Use **esc r** to disable a cell
- Use **esc y** to reactivate it
- Use **esc m** to go to markdown mode. Markdown is the typesetting language used in jupyter notebooks. In a markdown cell, double tap the mouse or glide pad (on your laptop) to go to edit mode.
- Shift + return to execute a cell (including markdown cells).
- If the equations don't typeset, try double tapping the cell again, and re-execute it.

## Links

- FNAL github site: <https://fnallpc.github.io/statistics-das/>

<!-- The indico page is: [https://indico.cern.ch/e/cmsdas2023](https://indico.cern.ch/e/cmsdas2023) -->

- The Mattermost for live support is: <https://mattermost.web.cern.ch/cmsdaslpc2024/channels/shortex-statistics>. (If you don't have access, see the general CMSDAS instructions for the Mattermost signup link.)

- The twiki is: <https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolLPC2024StatisticsExercise>


