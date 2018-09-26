import unittest
from search.haystack import HaystackCollection, Operator


class TestStringSearch(unittest.TestCase):

    def setUp(self):
        input_strings = [
            'this is some test string',
            'this is another test string',
            'this is yet another test string'
        ]
        self.haystacks = HaystackCollection(input_strings)

    def test_find_containing_all_strings(self):
        self.assertEqual(
            self.haystacks.search(Operator('AND'), ['another', 'test']),
            [1, 2]
        )

        self.assertEqual(
            self.haystacks.search(Operator('AND'), ['yet', 'another']),
            [2]
        )

    def test_find_containing_any_strings(self):
        result = self.haystacks.search(Operator('OR'), ['yet', 'another'])
        self.assertEqual(result, [1, 2])
