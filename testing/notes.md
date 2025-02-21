# Setup

I won't be the first one to say it, but package management sucks with python. To setup the environment for this lesson, execute the following commands:

```bash
# make sure you're in mini-lessons/testing/ first
python -m venv venv # python3 for unix-based systems
source venv/bin/activate
pip install -r requirements.txt
```

Essentially, this creates a virtual environment to install packages into so you don't have to install packages globally.

# Why Write Tests

When you write a piece of code, how do you know it works? Genuinely. Outside of just "knowing" it works, usually you write some quick tests for it. Does your code look like [version 0](src/v0.py)? If so, you know the hassle. You write a quick test, then inspect the output in the terminal, then continue on with your day. It works well enough for solo or small projects, but anything past that and this cycle of write, run, check, is not only extremely inefficient, but also leads to some -- if not many -- bugs falling through the cracks. Theres a whole heap of problems that come with this method of testing, including but not limited to:

-   Needing to physically check the output by hand, taking time and possibly missing small errors
-   Needing to comment out irrelevant tests from other developers or temporarily broken tests due to development
-   Needing to rewrite tests to properly construct the new version and call many functions outside of the desired function to test, making validating results difficult (as you don't know which part caused the error)

> Side note: you could counter some of these by writing `if` statements, throwing errors on unexpected outputs, creating lists of inputs and desired outputs, etc., etc., but at that point, you're essentially reinventing the wheel instead of leveraging already designed and highly robust testing suite. You'd also still be missing out on a lot of the best features of testing such as mocking and unit testing.

If you've encountered a single one of these -- and unless you're a prodigy, you have -- then you should consider more formal testing.

# Setting up Tests

So you want to write tests. How do you do that? Well, unfortunately we can't just immediately jump into that yet. We first have to pick our testing library that we'll be using for your program. For some languages (go, python), the testing suite comes pre-installed and ready to go, for others (javascript), there's clearly popular choices of which library to go with, and for the rest you need to carefully consider the pros and cons of the library that best fits your needs. For the purposes of this lesson, I actually use python's non-default testing library in favor of `pytest`, as it is simpler and less verbose.

With that out of the way, we can now start writing tests. Almost. The last thing we need to do is read the documentation from our suite of choice to figure out how to set up tests. With most suites, you'll need to name directories, files, classes, and functions a very specific way for it to be detected. In some cases, you might even need special parameters for the test functions.

**Now** we can write some tests.

# Writing Tests
