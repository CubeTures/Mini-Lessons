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

    # 
    print("4/2 =", calc.divide(4, 2))
    print()
