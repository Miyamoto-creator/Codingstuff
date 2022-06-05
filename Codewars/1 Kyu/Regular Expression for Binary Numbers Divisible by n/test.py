import codewars_test as test
from solution import regex_divisible_by
import re

@test.describe("Sample tests")
def sample():
    for i in range(1, 19):
        @test.it(f"Should work for n={i}")
        def _():
            reg = re.compile(regex_divisible_by(i))
            # Just a small sample test
            for x in range(5, 13):
                test.assert_equals(bool(reg.search(bin(x)[2:])), x % i == 0,
                    f'Your result for n={i} was incorrect when matched against {x}')