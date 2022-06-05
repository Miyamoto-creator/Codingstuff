import unittest   # The self framework
from solution import *

class Test_kebabize(unittest.TestCase):
    def test_kebabize(self):
        self.assertEqual(kebabize('myCamelCasedString'), 'my-camel-cased-string')
        self.assertEqual(kebabize('myCamelHas3Humps'), 'my-camel-has-humps')
        self.assertEqual(kebabize('SOS'), 's-o-s')
        self.assertEqual(kebabize('42'), '')
        self.assertEqual(kebabize('CodeWars'), 'code-wars')