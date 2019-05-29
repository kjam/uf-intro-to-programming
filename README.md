## University of Florida Audience Analytics: Introduction to Programming 

Welcome to the code repository for MMC6936: Introduction to Programming with Data. 

For more information on the course, please see the Canvas page.

### Special Note

The initial version of this course was 12 weeks instead of 16, meaning the numbers in these notebooks don't always match what you see on the video and might contain erroneous references to other modules if the number is used. Other than the name, the notebooks should be the same; so I hope this is not a source of great confusion.

If you find an erroneous reference in these notebooks to another module, please let me know or feel free to send a pull request! :)

### Installation

These lessons has been tested for Python 3.6 and primarily uses the latest release of each library, except where versions are pinned. You likely can run most of the code with older releases, but if you run into an issue, try upgrading the library in question first. 

First you will need to [install Conda for your OS](https://conda.io/docs/installation.html).

Then, to install all the requirements, we will setup a conda environment. You can do so and install all the requirements like so:

```
conda create -n py3data --copy python=3.6
source activate py3data
pip install -r install_reqs.txt
```

Then, when you want to run code you will need to make sure you are in your environment. To do so, you will type:

```
source activate py3data
```

In addition, you will need to install [sqlite3](https://www.sqlite.org/).

### Repository structure

Each module has it's own folder, from our precoursework (`module_00/`) to our final module (`module_12`). We also have a folder for data and a configuration folder (which you will learn about when we talk about APIs!)

### Python2 v. Python3

This repository has been built with Python 3. If you are using Python 2 and need help porting some logic or finding alternatives, please let me know and I will try and help. :)

### Corrections?

If you find any issues in these code examples, feel free to submit an Issue or Pull Request. I appreciate your input!

### Questions?

Reach out to @kjam on Twitter or GitHub or via her UF email. 
