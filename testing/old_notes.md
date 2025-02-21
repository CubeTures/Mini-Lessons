# What is Testing

Chances are, you've run into testing already. If you're in my class, you run tests on the functions you create for programming assignments to see whether you've implemented them correctly. So besides for grading an assignment written by a student, why would you use testing?

# Test Driven Development

Test driven development is one of the ways of creating applications and the perspective I'll be discussing for the purposes of this lesson. Test driven development is the act of creating tests before writing the code, writing the code, and the ensuring you wrote it correctly using the test case. Now, you're free to make as many mistakes as you want until you see that sweet green check mark next to your test case, and also can change the implementation of the code in the future without worrying about "regression" of your code. But, this is all assuming you wrote good test cases in the first place.

# Anatomy of a Good Test

A good test case covers all of your bases. I'm talking standard cases, weird cases, edge cases, corner cases -- at least one from every bucket, but usually more. For example, if I were testing a calculator with a divide function as follows:

```python
def divide(a: int, b: int) -> int:
    return a // b
```

I'd want to test `div(4, 2)`, `div(2, 1)`, `div(2, 3)`, `div(1, 1)`, `div(0, 1)`, `div(1, 0)`, `div(0, 0)`. Now that's a lot of test cases for a single line of code, isn't it? However, using this I catch all multiple things: first it doesn't handle fractions properly, and second it throws an error on 0 in the denominator. These test cases captured a wide enough breadth such that I understood where my implementation was lacking and I was easily able to correct it when needed. Now that we have the concept out the way, let's get into actually applicable instances.

# Unit Testing

From here on our, let's say we have [a simple CRUD app](src/crud.py) (so simple it doesn't even have an update function) that interfaces with [a local database](src/database.db) (it can be opened using SQLite).