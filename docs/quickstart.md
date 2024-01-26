---
layout: page
title: Quickstart
---

# Quickstart

MakeShift is a tool for procedural generation of text and phrases. It takes a template, written with plain text and a simple set of rules, and makes filled-out text and phrases for whatever you want to create.

The quickest way to get started is to read through the [Templates By Example](templates.md) page, and then head over to the [Lab](lab.md) to try it out.

## Installation Requirements
Building and running MakeShift on your own computer requires Python3.11 or higher. With Python installed, use Pip to install the MakeShift module from [PyPi](https://pypi.org/project/makeshift/). I recommend doing this in a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html).
```bash
> pip install makeshift
```

You can call `makeshift` from the command-line and provide a phrase template file to generate a random result.
```bash
> makeshift "/path/to/my_template.txt"
```

You can also download the MakeShift repository from [https://github.com/MJoseph1234/makeshift](https://github.com/MJoseph1234/makeshift)