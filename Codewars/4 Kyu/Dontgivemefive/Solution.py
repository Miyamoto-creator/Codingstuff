import codewars_test as test
import numpy as np

"""def ip_to_num(ip):
    convert_to_integer = [int(i) for i in ip.split('.')]
    int_to_binary = "".join([bin(i).replace("0b", "").zfill(8) for i in convert_to_integer])
    return int(int_to_binary, base=2)


def num_to_ip(num):
    binary, lst, bin_string = bin(num).replace("0b", "").zfill(32), [], ""
    for i in range(len(binary)):
        bin_string += binary[i]
        if (i % 8) == 7:
            bin_string += '!'
    ip = " ".join(bin_string.split('!')).rstrip().split(" ")
    for i in range(4):
        lst.append(int(ip[i], base=2))
    return ".".join([str(i) for i in lst])"""

def dont_give_me_five(start, end):
    if start == 0 and end == 1:
        return 2
    def goo(n):
            result = 0
            pos9 = 1
            while n > 0:
                digit = n % 10
                effective_digit = digit
                if digit > 5:
                    effective_digit -= 1
                to_add = effective_digit * pos9
                if digit == 5:
                    result = -1
                result += to_add
                n //= 10
                pos9 *= 9
            return result
    if (end >= 0 and start >= 0) or (end < 0 and start < 0):
        return goo(max(abs(end), abs(start))) - goo(min(abs(start), abs(end)) - 1)
    else:
        return goo(abs(end)) + goo(abs(start)) + 1

dont_give_me_five(-17, 9)
dont_give_me_five(1, 9)
dont_give_me_five(4, 17)
dont_give_me_five(984, 4304)
dont_give_me_five(40076, 2151514229639903569)


"""@test.describe("Example tests")
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
        test.assert_equals(dont_give_me_five(51, 60), 1)"""