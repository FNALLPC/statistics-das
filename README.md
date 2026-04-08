# FNAL LPC CMS Data Analysis School (CMSDAS): Statistics Short Exercise

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
| [`6/exercise_6.ipynb`](6/exercise_6.ipynb) | histogram template analysis using `combine` |

## Setup Instructions

1. Go to https://coffea.casa and log in with your CMS credentials.
2. Start a new server with the image named `Combine / Python 3.10 / ROOT 6.26.4`.
3. In the terminal window, download the tutorials by typing:
    ```bash

    git clone https://github.com/FNALLPC/statistics-das.git
    ```
    Make sure to use https and NOT ssh on `coffea.casa`.
4. To open a notebook, e.g. `statistics-das/0/exercise_0.ipynb`, simply click on the file.
5. When using `combine` or `text2workspace.py` you may encounter "command not found" error. If so, open a terminal and update the following environment variables:

    ```
    export PATH=$PATH:/tmp/HiggsAnalysis/CombinedLimit/build/bin/

    export LD\_LIBRARY\_PATH=$LD\_LIBRARY\_PATH:/tmp/HiggsAnalysis/CombinedLimit/build/lib/

    export PYTHONPATH=/tmp/HiggsAnalysis/CombinedLimit/build/lib/python

    ```
6. Have a coffee.

## Notebook Tips
Jupyter notebooks are structured into **cells**. It is recommended that you execute the notebooks one cell at a time to ensure that each cell works as expected. And, yes, cells should be executed sequentially! Of course, if you're careful, you can go back and re-execute cells. But remember jupyter notebooks are ``sticky'' in that the notebook pays attention to the order in which cells have been executed. This can lead to confusion. If things get really messed up, it's usually better to re-launch the jupyter kernel and start again from scratch.

### Some useful shortcuts
- Use **esc r** to disable a cell
- Use **esc y** to reactivate it
- Use **esc m** to go to markdown mode. Markdown is the typesetting language used in jupyter notebooks. In a markdown cell, double tap the mouse or glide pad (on your laptop) to go to edit mode.
- Shift + return to execute a cell (including markdown cells).
- If the equations don't typeset, try double tapping the cell again, and re-execute it.

## Links & Resources

- [Exercise repository on github](https://fnallpc.github.io/statistics-das/)

- [2026 LPC CMS DAS lecture slides](https://docs.google.com/presentation/d/1T0HE6yzK9QDwYwkF1R8JcbIxuclV4meg_ahavk1Yf8g/edit?usp=sharing)

- [Legendary 2023 LPC DAS lecture slides](https://docs.google.com/presentation/d/1MF4gwFe9XNc-qQI6ea_BX6gKyWk93MvPhcSmIeCU49A/edit?slide=id.p#slide=id.p)

- [Javier Duarte's lecture slides](https://twiki.cern.ch/twiki/pub/CMS/SWGuideCMSDataAnalysisSchoolLPC2025StatisticsExercise/CMSDAS2019_Statistics_14Jan2019_%281%29.pdf)

- [Nick Wadle's  2022 HCP Summer School slides](https://indico.fnal.gov/event/54596/contributions/248583/attachments/159060/208956/statistics.pdf)
