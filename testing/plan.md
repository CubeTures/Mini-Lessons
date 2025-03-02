# Unit Testing

-   Test driven development
-   Do in python
-   What is unit testing
    -   Why unit test
-   Types of testing
    -   Unit testing
    -   Integration testing
    -   Dependency Injection
        -   Monkey Patching

```bash
python3 -m venv venv
source venv/bin/activate.fish
pip install -r requirements.txt

coverage -m pytest
```

# Story

-   We have some code, how do we test its validity? `v0`
    -   (code with bugs, visual inspection is never enough)
    -   Sad, sad testing without a library `test_v0`
    -   Pros of testing
-   Write a test `test_v1`
    -   Code without bugs `v1`
    -   What should go into a test
    -   Cool features
-   Now we want to extend our app `v2` (and have tests to go with it `test_v2`)
    -   We've just accidentally created another integration test
    -   Different types of testing
-   The dependency issue
    -   Mock the connection `v3` and dependency injection for setup `test_v3`
    -   Decorators for optimal testing `test_v4`
    -   Meta programming: "A programming technique that allows programs to modify or create other code."
