from src.example import add_two


class TestExample:
    def test_simple(self):
        assert add_two(3, 4) == 7
