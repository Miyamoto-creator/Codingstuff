import codewars_test as test


class Solution:
    pass


def title_case(title, minor_words=''):
    title, minor_words = title.lower().split(" "), minor_words.lower().split(" ")
    for i, n in enumerate(title):
        title[i] = n.capitalize()
        if i > 0 and (n in minor_words):
            title[i] = n.lower()
    senor = [n.lower() for i, n in enumerate(title) if i > 0 and n in minor_words n.capitalize()]
    return str(" ".join(senor))


So = Solution()
title_case('THE WIND IN THE WILLOWS', 'The In')
title_case('a clash of KINGS', 'a an the of')
title_case('the quick brown fox')

@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        test.assert_equals(title_case(''), '')
        test.assert_equals(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
        test.assert_equals(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
        test.assert_equals(title_case('the quick brown fox'), 'The Quick Brown Fox')
