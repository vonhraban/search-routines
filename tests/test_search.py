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

        self.assertEqual(
            string_search.find_indices_containing_all_of(['another', 'test']),
            [1, 2]
        )

        self.assertEqual(
            string_search.find_indices_containing_all_of(['yet', 'another']),
            [2]
        )

    def test_find_containing_any_strings(self):
        input_strings = [
            'this is some test string',
            'this is another test string',
            'this is yet another test string'
        ]
        string_search = StringSearch(input_strings)

        result = string_search.find_indices_containing_any_of(['yet', 'another'])
        self.assertEqual(result, [1, 2])


