import unittest
import m2lexer.utils

class TidGeneratorTestCase(unittest.TestCase):

    def setUp(self):
        self.MAX_TOKENS = 10
        
    def tearDown(self):
        pass

    def test_generator_creation(self):
        result = m2lexer.utils.TidGenerator(self.MAX_TOKENS)
        self.assertIs(type(result), m2lexer.utils.TidGenerator)
        self.assertEqual(result.MAX_TOKENS, self.MAX_TOKENS)

    def test_unique_tids(self):
        tid_gen = m2lexer.utils.TidGenerator(self.MAX_TOKENS)
        result1 = tid_gen.generate_tid()
        result2 = tid_gen.generate_tid()
        self.assertNotEqual(result1, result2)

    def test_max_tokens(self):
        tid_gen = m2lexer.utils.TidGenerator(self.MAX_TOKENS)
        for x in range(self.MAX_TOKENS):
            tid_gen.generate_tid()

        with self.assertRaises(StopIteration):
            tid_gen.generate_tid()

