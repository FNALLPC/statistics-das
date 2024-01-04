---
title: Setup
---
> ## Github repo and Mattermost
> - The following instructions are also given in the README: [https://github.com/FNALLPC/statistics-das/blob/master/README.md](https://github.com/FNALLPC/statistics-das/blob/master/README.md)
> 
> - Join the Mattermost channel and feel free to ask questions: <https://mattermost.web.cern.ch/cmsdaslpc2023/channels/shortexstatistics>
{: .callout}

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
3. Configure container environment parameters and click on "start session"
> 
> you can use the defauly parameters: (Software Stack: 104a, Platform: CentOS 7 (gcc 11), Number of cores: 4, Memory: 8 GB, Spark cluster: None)
4. On the upper right corner, click on "`New Terminal >_`" button. This opens a new tab with a terminal
5. In the terminal window, download the tutorials by typing:
```bash
git clone https://github.com/FNALLPC/statistics-das
```
6. In the original tab, click on "CERNBox" button at the top
> ## Hint!
> If you want to cut-and-paste this command in the terminal, highlight the link and copy it as you usually would <kbd>Ctrl</kbd>+<kbd>c</kbd> or <kbd>⌘</kbd>+<kbd>c</kbd>. To paste it, use <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>v</kbd>  or <kbd>Shift</kbd>+<kbd>⌘</kbd>+<kbd>v</kbd>
7. Now go back to the Jupyter directory tab. There should be a new directory called `statistics-das`. All of the tutorials and exercises are in there. You can directly run one of them by opening them, e.e. `statistics-das/0/exercise_0.ipynb`

<!--Start by clicking on `setup-libraries.ipynb` and running it.-->

<!-- Inserting some whitespace at the end -->
<p style="height: 100px"></p>

{% include links.md %}
