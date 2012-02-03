import unittest
import m2lexer.tokens.token
from m2lexer.utils import TidGenerator

class TokenTestCase(unittest.TestCase):

    def setUp(self):
        self.tid_gen = TidGenerator(999999)

    def tearDown(self):
        pass

    def test_token_creation(self):
        tid = self.tid_gen.generate_tid()
        result = m2lexer.tokens.token.Token(tid)
        self.assertIs(type(result), m2lexer.tokens.token.Token)
        self.assertEqual(tid, result.tid)
