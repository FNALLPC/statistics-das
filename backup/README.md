# CMS Data Analysis School (CMSDAS): Statistics Short Exercise

## Introduction

This is a set of tutorials for the CMS Data Analysis School (CMSDAS) Statistics Short Exercise that are implemented in Jupyter notebooks. The tutorials provide a concise introduction to key ideas in statistics and a few of the statistical analysis tools commonly used in high-energy physics.

## Notebooks

| __notebooks__   | __description__     |
| :---          | :---        |
| [`0/exercise_0.ipynb`](0/exercise_0.ipynb) | a very short `PyROOT`/`RooFit` tutorial | 
| [`1/exercise_1a.ipynb`](1/exercise_1a.ipynb) | analyzing a single count using `RooFit`/`RooStats`  |
| [`1/exercise_1b.ipynb`](1/exercise_1b.ipynb) | analyzing a single count using `RooFit`/`RooStats`  |
| [`2/exercise_2.ipynb`](2/exercise_2.ipynb) | analyzing three counts using `RooFit`/`RooStats` |
| [`3/exercise_3a.ipynb`](3/exercise_3a.ipynb) | analyzing three counts using `combine` | 
| [`3/exercise_3b.ipynb`](3/exercise_3b.ipynb) | a realistic counting experiment using `combine` | 
| [`3/exercise_3c.ipynb`](3/exercise_3c.ipynb) | systematic uncertainties for data-driven background estimates using `combine` |
| [`4/exercise_4.ipynb`](4/exercise_4.ipynb) | binned fit to Run I H->gg data (optional) | 
| [`5/exercise_5.ipynb`](5/exercise_5.ipynb) | unbinned fit to Type Ia supernovae distance modulus/red shift data (optional) |
| [`6/exercise_6.ipynb`](6/exercise_6.ipynb) | histogram template analysis using `combine` (optional) |

## Getting Started on Coffea-casa

1. Go to https://coffea.casa and log in with your CMS credentials.
2. Start a new server with the "Combine / Python 3.10 / ROOT 6.26.4" image.

You're all set!
For any notebooks that use `combine` or `text2workspace.py` you may encounter "command not found" error. If so, add the following lines to a new cell in your notebook and run it:
```python
import os

os.environ["PATH"] = os.environ["PATH"] + ":/tmp/HiggsAnalysis/CombinedLimit/build/bin"
os.environ["LD_LIBRARY_PATH"] = os.environ["LD_LIBRARY_PATH"] + ":/tmp/HiggsAnalysis/CombinedLimit/build/lib"
os.environ["PYTHONPATH"] = "/tmp/HiggsAnalysis/CombinedLimit/build/lib/python"
```

## Getting Started on [Swan](http://swan.web.cern.ch/)

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
7. Open and execute the contents of setup-libraries.ipynb
8. To open a notebook, e.g. `statistics-das/0/exercise_0.ipynb`, simply click on the file.

If you face compilation or jupyter kernel errors when running `combine` from the jupyter notebook in exercise 3, you can compile the `combine` tool in the `Swan` terminal by doing `source build-combine-standalone.sh`.

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


