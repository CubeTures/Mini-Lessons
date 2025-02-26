# Setup

If you want to run the tests for this lesson on your machine, you'll have to do the following (yes, it's cumbersome, but that's just python in a nutshell):

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

> Side note: you could counter some of these by writing if statements, throwing errors on unexpected outputs, creating lists of inputs and desired outputs, etc., etc., but at that point, you're essentially reinventing the wheel instead of leveraging already designed and highly robust testing libraries. You'd also still be missing out on a lot of the best features of the libraries such as mocking and unit testing.

If you've encountered a single one of these -- and unless you're a prodigy, you have -- then you should consider more formal testing.

# Setting up Tests

So you've decided you want to write some tests. How do you do that? Well, unfortunately we can't just immediately jump into that yet. First, you have to pick the testing library that you'll be using for your program. For some languages (go, python), the testing library comes pre-installed and ready to go, for others (javascript), there's a clearly popular choices of which library to go with, and for the rest you'll need to carefully consider the pros and cons of the library that best fits your needs. For the purposes of this lesson, I actually use python's non-default testing library in favor of `pytest`, as it is simpler and less verbose.

With that out of the way, we can now start writing tests. Almost. The last thing we need to do is read the documentation from our library of choice to figure out how to set up tests. With most libraries, you'll need to name directories, files, classes, and functions a very specific way for it to be detected. In some cases, you might even need special parameters for the test functions.

**Now** we can write some tests.

# Writing Tests

A good test suite will cover as many test cases as possible, from expected cases, to

-   Cover as many cases as possible
-   Don't be dependent

Now that we've covered our bases when it comes to testing, let's get into the cool stuff.

# Types of Tests

-   Unit tests
-   Integration tests
-   End to end tests
-   Regression tests

# Dependency Injection

-   Decorators

How to show case:

-   First show case of duplicate and dependent code in v1, where delete and put rely on their previous tests
-   Then show how to mock and show this can be eliminated by initializing the database with values in the `setup_method`
-   Then show how this can be expanded upon to method dependant by using decorators
    -   Particularly useful with `get_all` and `get_count`
    -   Moving the declaration to `setup_method` is a sort of win some lose some, but with decorators we overcome the extra boilerplate required by the lose, making it all win

```python
from functools import wraps

def with_db_data(data):
    """Decorator to automatically set up a database with given data before test."""
    def decorator(func):
        @wraps(func)
        def wrapper(db_session, *args, **kwargs):  # Inject db_session fixture
            db_session.add_all(data)
            db_session.commit()
            return func(db_session, *args, **kwargs)
        return wrapper
    return decorator

@with_db_data([User("Alice"), User("Bob")])
def test_users_in_db(db_session):
    users = db_session.query(User).all()
    assert len(users) == 2
```