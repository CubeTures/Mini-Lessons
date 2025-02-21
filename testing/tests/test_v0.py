import pytest
from src.v0 import Calculator

# directories, files, classes, and functions
# need to be named in a specific way in order
# for the testing suite to detect them.
# This is true for most languages and their
# premier suites.


class TestCalculator:
    # this special method runs before every test case
    # this is handled by the testing suite
    def setup_method(self):
        self.calc = Calculator()

    # use an assert statement to throw an error when it is false
    def test_divide_no_remainder(self):
        assert self.calc.divide(4, 2) == 2

    # incorrect test cases get marked in the IDE
    def test_divide_with_remainder(self):
        assert self.calc.divide(2, 3) == 2 / 3

    # include strings to further explain the desired output
    def test_divide_by_one(self):
        assert (
            self.calc.divide(2, 1) == 1
        ), "Returned value should be the same value as parameter a"

    # mark tests as todo to skip them without commenting out the whole thing
    @pytest.mark.skip(reason="TODO")
    def test_divide_by_itself(self):
        pass

    # automatically fails on unexpected exceptions
    def test_divide_zero(self):
        assert self.calc.divide(0, 1) == 0

    # use the suite to expect an error being raised
    def test_divide_by_zero_fails(self):
        with pytest.raises(Exception):
            self.calc.divide(1, 0)
