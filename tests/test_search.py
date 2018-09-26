import unittest
from search.search import StringSearch


class TestStringSearch(unittest.TestCase):

    def test_find_containing_all_strings(self):
        input_strings = [
            'this is some test string',
            'this is another test string',
            'this is yet another test string'
        ]
        string_search = StringSearch(input_strings)

        result = string_search.find_indices_containing_all_of(['another', 'test'])
        self.assertEqual(result, [1, 2])


