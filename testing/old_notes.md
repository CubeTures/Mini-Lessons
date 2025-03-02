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

A good test suite will cover as many test cases as possible. From expected cases, to edge cases, corner cases, invalid cases, and beyond.

-   **Expected Cases**: cases you would expect no issues to arise from
-   **Edge Cases**: cases that trigger your "else" statements, hard to reach areas in the code, or otherwise known problematic inputs
-   **Corner Cases**: cases that stress the algorithm to the limit, hitting multiple edge cases at once
-   **Invalid Cases**: when you expect and error to be thrown or otherwise invalid inputs

Observe [test suite v0](tests/test_v0.py) for an example list of these cases. It not only has a couple expected cases but odder cases like `1 / 1` before getting into the obvious error of `1 / 0`, where it even expects an error to be thrown of type `ZeroDivisionError` (a particularly useful feature, as it ensures the caller of a function receives the correct information to properly recover). In summary, it covers all cases to make sure when used in production by many different users, no unexpected errors arise.

# Types of Tests

There are multiple types of tests that you should be aware of before writing a test. They each serve their own purpose.

First off is the unit test. These are small unit tests that test individual functions that run quickly. You want to avoid as many external dependencies as possible (more on the later). The idea is that these are functions you can run after finishing writing every code block to see if things haven't broken. Connecting to expensive services or doing computationally heavy tests here would dissuade that.  

Next is the integration test. Think of this as testing the "boundaries" of your code. It makes sure your code works properly with external services, but only that. If you wrote a class that calls a database and then return the raw data for other classes to process, your tests should be handling that raw data. Remove as many abstraction layers between your calls and the test, as this is to ensure only the very edges of your program where necessary. These tests should be higher in complexity, take longer to execute, and be less abundant than your unit tests.

Finally, the end-to-end test. This is a complete, fully encompassing test for your program. Some tests like this include UI tests where you write a set of recorded actions that will be taken and a script will play them back to you, expecting the UI to reflect as you tell it. It is how the user will interact with the program; not worrying about individual functions but rather the overall picture. There should be few of these and they will be slow.

As a bonus, I'll quickly discuss regression testing. This testing is not necessary a new type, but rather something to be looking for. Regression, according to oxford dictionary, means "a return to a former or less developed state." For testing, the meaning is similar: does your code no longer pass the test case? If you wrote a function, passed all the test cases, then changed the function later so that it no longer passes the cases, then what you just experienced is regression. And, regression testing is what just saved you from multiple hours of debugging.

# The Dependency Issue

- You want to make a unit test of a function that eventually calls an external resource
    - Suppose I have a new class, users, that takes data from the database and transforms them into users
    - At the moment this is a bad integration test, as it utilizes external sources but . But, we already know our connection works; we've done plenty of integration 
- To prevent it from becoming an integration tests, use mocking and dependency injection
- Mocking is the act of replacing external dependencies with simulated, fake versions you have control over
- Mocking is implemented using dependency injection


You should always strive to make every test as independent and modular as possible. In the best case, your test will follow the format Arrange, Act, Assert. This means you will first set up the conditions, perform the necessary calls, then assert the returned values. To showcase this, consider [test suite v1](tests/test_v1.py). This time around, we're looking at a [more practical codebase](src/v1.py) of a CRUD app that interfaces with an SQLite database. It Arranges the data in `setup_method`, then Acts by calling functions, and finally Asserts the expected return value (or lack thereof).

> If you didn't understand a few of those terms, just know we're concerned with Creating, Reading, Updating, and Deleting (CRUD) information from a storage of data (a database). The term Put has been used in place of Creating and Updating, as it can both create or update data, decreasing the complexity of the program (updates are difficult to write).

Here, it's actually difficult to make the tests independent of one another. Since all our data is being reset each test, we have to first put the data then attempt to read it, and we must first put the data before we attempt to delete it. This is the exception rather than the norm, however.

Your goal should always be to make your tests (as in your testing suite) call as few other (if any) functions as possible. You should be testing a single function and its expected input and output rather than how it reaches that output. In other words, we don't want to concern ourselves with how the function operates by setting up what we know it will need, instead we should be giving it the tools it needs to get our expected output on its own. So, how would we do that?

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

# Conclusion

Testing is important. So important, that some people follow a methodology called "Test-Driven Development." In this, the test cases are written before the actual function is. How can you know if your code works without passing all the tests cases? This methodology only works after following the guidelines listed above, however: without covering many cases, your tests don't reflect how your function will be used; without dividing tests into unit and integration, programmers will run tests less frequently and encounter more bugs; without dependency injection, your 