import codewars_test as test
from tacofriday import dont_give_me_five


@test.describe("Example tests")
def test_group():
    @test.it("small_numbers")
    def test_case():
        test.assert_equals(dont_give_me_five(-17, 9), 24)
        test.assert_equals(dont_give_me_five(1, 9), 8)
        test.assert_equals(dont_give_me_five(4, 17), 12)
        test.assert_equals(dont_give_me_five(-17, -4), 12)

    @test.it("larger_numbers")
    def test_case():
        test.assert_equals(dont_give_me_five(984, 4304), 2449)
        test.assert_equals(dont_give_me_five(2313, 2317), 4)
        test.assert_equals(dont_give_me_five(-4045, 2575), 4819)
        test.assert_equals(dont_give_me_five(-4436, -1429), 2194)

    @test.it("huge_numbers")
    def test_case():
        test.assert_equals(dont_give_me_five(40076, 2151514229639903569), 326131553237897713)
        test.assert_equals(dont_give_me_five(-206981731, 2235756979031654521), 340132150309630357)
        test.assert_equals(dont_give_me_five(-2490228783604515625, -2490228782196537011), 520812180)
        test.assert_equals(dont_give_me_five(-9000000000000000000, 9000000000000000000), 2401514164751985937)

    @test.it("edge_cases")
    def test_case():
        test.assert_equals(dont_give_me_five(0, 1), 2)
        test.assert_equals(dont_give_me_five(5, 15), 9)
        test.assert_equals(dont_give_me_five(-5, 4), 9)
        test.assert_equals(dont_give_me_five(51, 60), 1)

test_group()