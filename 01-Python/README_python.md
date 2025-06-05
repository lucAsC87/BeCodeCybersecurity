# Learn Python

Python is one of the trendiest programmation language for the moment. Easy to learn, Python is often used as an example while learning programmation.

## Deadline inclusive of Project

20 May 2025 -29 May 2025.

## What is Python?

Python is a programming language invented by Guido Van Rossum. The first version of Python was released in 1991.

### Python is an interpreted language!
The main difference between a compiled and an interpreted language is as follows : while the compiler translate once for all a source code into an independent executable file (therefore using machine code or assembly code), the interpreter is needed 
at each launch of the interpreted program, to translate.

The interpreter translates a portion of code, executes it and translates then the next portion of code, executes it, and so on. If you have already taken a little look at  programming, you might find that this language has a certain poetry. Programmers often have fun looking for the nicest/most effective way to write a sequence of instructions.

### What does Python do?
Python is both simple and powerful, it allows you to write very simple scripts but thanks to its many librairies, you can also work on more ambitious projects.

* Web: Today Python combined with the framework Django is a very accurate technological choice for big websites projects.
* System: Python is also frequently used by system admins to create so-called repetitive tasks or simply maintenance tasks. Besides, if you want to create Java applications coded in Python, it is possible thanks to the Jython project.

### Why would you choose Python over other languages?
Python is a language that’s easy to learn and its code is more readable, and so easier to maintain. It can be up to 5 times more concise than Java language for instance, which boosts the developer productivity et reduce mechanically the amount of bugs.
Python is also used in the science community, for example bioinformatics. Libraries are available for this domain as the biopython module. 

There are also libraries that facilitates the creation of 2D (and 3D) video games. For instance : [pyGame](http://www.pygame.org/news.html)

On the other hand, as Python is an interpreted language, it’s logically slower than a compiled one. Even though great efforts have been made lately, for very big projects, it may be necessary to use Java, C#, etc.

A last thing to know about Python : its environnement is open, meaning it can work with Java, C++, C#, and so on. 


## Installation

### Anaconda

To make your life easier, please download and use Anaconda on Windows. It comes with all necessary support to install and manage a wide range of scientific computing packages, including libraries for data manipulation, machine learning, visualization, and more.

**Recommended:** [Please follow this link for Anaconda on Windows](https://docs.anaconda.com/free/anaconda/install/windows/)

If you want to install Anaconda on Linux, [follow these guidelines](https://docs.anaconda.com/free/anaconda/install/linux/).

### Miniconda

If you want a minimal distribution instead of Anaconda (it may be a little too heavy with all packages), you may try to install [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) instead. Note that in case of Miniconda, you may have to install a lot of additional Python libraries (especially for data manipultation, machine learning, etc.) on your own, using the `conda` package manager. Thus, for ease, Anaconda is still recommended.

### Advanced

In case you are interested in installing everything separately on your system (only recommended if you are comfortable with similar approaches for other software packages on your operating system), you may follow these steps. Else, install Anaconda.

#### Install Python

*If you install Anaconda or Miniconda, this step is not needed.*

**Linux or MacOS:** If you work in a Linux or MacOS environment, good news -- Python is already installed. However, make sure you have version `3.xx`. Check via terminal.
```shell
python -v
```

**Windows:** You can download a Python installation file at this address: [Download Python](https://www.python.org/download/)

#### Which version to choose?
Try to use the most recent/stable version. Note that the most used version those days is `3.xx`. There are [compatibility problems between the version 2 and 3 of Python](https://learntocodewith.me/programming/python/python-2-vs-python-3/). Therefore it is advised that you learn Python 3 and then learn the differences between the two versions. This way, you’ll be able to handle code from previous version, if at all needed.

#### Install Jupyter-Notebook

*If you install Anaconda, this step is not needed.*

Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

[Download and install Jupyter-Notebook](https://jupyter.org/)

To launch the notebook interface, open your terminal and type:
```shell
jupyter-notebook 
```

## Editors and IDEs

If you want to use Jupyter Notebook via the browser based interface, you will find it as a native application on Windows after you install Anaconda. You may also open it via the Anaconda Navigator application on Windows.

However, you can also use your favorite programming IDE to work with python (`.py` files) or jupyter notebooks (`.ipynb` files). But
[Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial) is recommended.

## Virtual Environments

Think of a virtual environment as a separate container for each Python project. Each container:

1. Has its own Python interpreter
2. Has its own set of installed packages
3. Is isolated from other virtual environments
4. Can have different versions of the same package

Using virtual environments is important because:

1. It prevents package version conflicts between projects
2. Makes projects more portable and reproducible
3. Keeps your system Python installation clean
4. Allows testing with different Python versions

Check the exercise [here](./0.Python_fundamentals/01.VirtualEnv/00.VirtualEnv.ipynb)



