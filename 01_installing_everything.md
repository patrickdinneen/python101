# Installing Python and associated tools

You'll need to have a terminal open for this.

You can open the default terminal (called `Terminal`) by opening Spotlight (cmd + space) and typing `terminal` 

## 0. Ensuring Homebrew is installed
Homebrew is a package manager for MacOS. It isn't installed by default.

It is invoked using the command `brew`

1. Type `which brew`. If you see a valid path you can proceed to the next stage. If not, continue.
2. Run: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

Congratulations! You have installed Homebrew

## 1. Install Python 3.7 using Homebrew

1. Run: `brew install python@3.7`
2. Run: `which python3` to confirm the current python path.

## 2. Download PyCharm Edu

[Free Download](https://www.jetbrains.com/edu-products/download/#section=pycharm-edu) from JetBrains

## 3. Creating a virtualenv

Virtual Environments are very important for keeping your sanity when working with Python. Similar to renv, this allows you to work with different versions of libraries on different projects.

We won't get into the details today, but we wil eventually.

1. Using the command `cd` navigate to the directory where you cloned this repo. Eg `cd work/learn/python101`
2. Type `pwd` to print the working directory and confirm where you are (not strictly necessary but all practice is good practice)
3. Create a new virtual environment. You'll only need to do this once per project. Run: `python3 -m venv .venv`
4. Activate your virtual environment. Run: `source .venv/bin/activate` 

## 4. Get started with IPython and Jupyter Notebooks

This section assumes that you are in the repo directory and have activated your virtualenv

1. Install required packages. Run `pip install -r requirements.txt`
2. Open an interactive Python shell with IPython. Run `ipython`. This is very much like the console in R. You can interactively write and run code. Very useful for exploratory work.
3. In IPython, run: `print('hello world!')'
4. Exit IPython, run: `exit`

Python has notebooks that are very similar to R, these are called Jupyter notebooks and can in fact have R code in them too.