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

Programming is difficult. Especially when dealing when outside libraries, bugs occur often and in unexpected places. Its our jobs as programmers to make sure we know our code works and is bug free. So how can we do that? We _could_ visually inspect it. Take [this code](src/v0.py) of a simple `CRUD` app. Can you find the bug in the code by visual inspection alone? Go ahead. Seriously. Give it a try. Done? Did you find the bug? Well, there's actually 3 bugs (sorry, I lied). Chances are you didn't find all of them, if you even found one of them.

So, visual inspection obviously doesn't work. Whats next? The natural instinct is to run the code. That's a good idea, actually. But the execution is often so poor it actually makes the project harder to maintain than if you just left the code as is. Observe [our sample "test suite"](tests/v0_test.py) for the code. Does this look familiar to you? Scattered print statements, comment carpet bombs for temporarily broken code, and a sad, sad initialization of required classes before running. On top of that, you'd have to visually inspect all the output every print statement. What if you have 100s of tests? Just delete the old ones once the function works? Ok, then what if your teammate, Jeff, comes in and unknowingly breaks the function you just deleted the tests for? Long story short, this type of testing is a headache for everyone involved and is unmaintainable in the long run or with teams of any size.

So, what can we do?

# Setting Up Tests

A testing library is a collection of tools and functions specifically made for the development of automated testing.

Libraries come in all shapes and sizes. Some languages come with libraries preinstalled (`python` with `unittest`, `go` with `stdlib`), other languages have clearly popular libraries (`javascript` with `jest`), and others have libraries you'll have to carefully consider the pros and cons of before choosing one for your project. For this lesson, I actually didn't use python's built-in library `unittest`, but instead an external library called `pytest`, as I believe it is clearer, simpler, and cleaner. Just remember: what works for one project may not necessarily work for another.

The next thing to know is that you have to name directories, files, classes, and functions properly in order for your test to be properly recognized by your library of choice. In some cases, you might even need special parameters for the test functions. Make sure to read your library's documentation before you get a headache just getting everything set up.

With that out of the way, let's write some tests.

# Writing Tests

Consider the [bug-fixed version of our previous code](src/v1.py). Let's write some tests to make sure it doesn't regress in the future.

When writing tests, it's important to cover a wide variety of test cases. Specifically, you should aim to cover several typically cases, some edge cases, a small batch of corner cases, and every error case you have. **Typical cases** are your standard tests, with simple inputs and outputs. **Edge cases** strive to touch the "else" cases of your if else statements. **Corner cases** hit as many else statements and odd parts of your function as possible. Finally, **error cases** are using inputs you know will cause an error to be thrown.

The idea is that you want to know your average, run of the mill inputs will work, then slowly work your way to less common inputs to make sure they function as intended. Finally, if you know your program should throw an error, make sure it actually does that.

To create the desired tests, we can leverage some cool library features to make our experience as enjoyable as possible. Read [our new test suite](tests/v1_test.py) (notice how our models have actually been placed into a [separate file](tests/v1_models.py) for cleaner code and so they can be reused in other tests). Some of these cool features include (but are not limited to) being able to use the UI to run tests, getting a marker when the test case didn't produce the expected output, an optional string explaining the desired output, skipping unfinished or currently broken tests, and expecting exceptions to be raised. We also get access to `setup_method()` that automatically gets called before every test in the class, which helps massively reduce boilerplate.

Using this vast set of features, we can make sure the code works as intended in all scenarios of usage.

# Types of Tests

So, now that our `CRUD` app works and is tested, we decided to expand our app to create a [user database](src/v2.py): a simple interface over our `CRUD` class to prevent us from working with raw data and dictionaries.

So, let's do as we did before and [write our test suite](tests/v2_test.py) for this new code! Except... something's off. Do you notice it? The whole idea of a test is to examine if a single function is working as intended, but here, we're still calling [our original code](src/v1.py)! As you can imagine, this is less than ideal. For example, if the tests we just wrote don't work, how can we be sure it was the function that has the error? It's entirely possible there's some mistake with the connection to our SQL database or original code, causing a chain reaction and giving us an error further down the line. That would be harder than necessary to debug, not to mention slower since it relies on the connection (and possibly expensive if you're using a cloud database). To remedy this issue, let's first understand the types of tests.

-   **Unit Tests**: Small, quick tests that check the validity of individual functions. They should be run frequently, and their speed is directly proportional to how often you're encouraged to run them. This is the type of test we want to use for our [`UserDB`](src/v2.py).
-   **Integration Tests**: Longer, more expensive tests that examine the "boundaries" of your code. They make sure your code properly interacts with external libraries or services. There should be minimal layers of abstraction between the test and the boundary to ensure the library is essentially "quarantined" from the rest of your code. This is the type of test we have set up for our [original code](src/v1.py).
-   **End-to-End Tests**: A complete, intensive test encompassing your program. Some examples include UI tests, where you record a list of actions on the UI and expect an output to occur. It's concerned less with the output of individual functions and more with the overall result (as a user would).

With this knowledge, its easy to see where we've gone wrong: we need to isolate our unit test from being an integration test. But, how can we do that?

# The Dependency Issue

What if we made [our own, synthetic version](src/v3.py) of our `CRUD` app? That way, instead of calling `read()` and then reaching our to SQL with the proper command, we'd just fake it and store our data in a python dictionary. This is called **mocking**. But after that, so what? We have a fake version, but how do we use it when testing and the real version when in production? Thats where **dependency injection** comes in.

Dependency injection is basically providing the objects that an object needs (its dependencies) instead of having it construct them itself. To accomplish this, we could rewrite our `UserDB` class to take in its constructor a pre-made `CRUD` so that we can instead pass it the mock version to it during instantiation:

```python
class UserDB:
    def __init__(self, database):
        self.db = database
```

Or... we could do the cooler option.

**Monkey patching** is a special method of dependency injection that works by dynamically replacing attributes at runtime. Read over [our final test version](tests/v3_test.py). Here, we utilize monkey patching to write over the imported class and replace it with our own function. The `UserDB` class will then unknowingly call this function we injected and in turn receive a valid (mocked) database. This way, not only can we remove our dependency on the original code, but we can remove the weird paradox we had before where we needed to use `put()` before we could test if `put()` works. We just have to pass in a list of users and viola! With that, we can now safely work on writing some awesome tests!

> Disclaimer: Monkey Patching only works with a small subset of languages (python, javascript, ruby, and some more) and has [many issues](https://en.wikipedia.org/wiki/Monkey_patch#Pitfalls) that have been discussed in the past. I just thought it was cool to show off. In reality, you should use the dependency injection method that works best for your project, which will vary. Do your research!

# Conclusion

Proper testing and techniques like mocking and dependency injection ensure your application is resilient without breaking first. Without a good testing suite, changing code is discouraged -- you'd never be able to tell if your rewritten code works and doesn't break any existing part of the application! With a good testing suite, coding new features is a breeze and refactoring is stress-free. In test-driven development, testing even comes before writing the actual code! Give it a try sometime, and familiarize yourself with your favorite programming language's top testing libraries. I can assure you, you won't regret it.
