class Calculator:
    # other functions omitted for brevity

    def divide(self, a: float, b: float) -> float:
        if a == 0 or b == 0:
            raise ZeroDivisionError()

        return a // b


# the quick and dirty way of running tests
# "just run the file and inspect the output"
if __name__ == "__main__":
    calc = Calculator()

    # test cases
    print("4/2 =", calc.divide(4, 2))
    print("2/3 =", calc.divide(2, 3))
    print("2/1 =", calc.divide(2, 1))
    print("1/1 =", calc.divide(1, 1))
    print("0/1 =", calc.divide(0, 1))
    print("1/0 =", calc.divide(1, 0))
