import unittest
from main import parse_args
from search.haystack import Operator


class TestMain(unittest.TestCase):

    def test_full_args_parsing(self):
        parsed = parse_args(['--file', 'filename', '--keywords', 'these are keywords', '--operator', 'OR'])
        self.assertEqual(parsed.file, 'filename')
        self.assertEqual(parsed.keywords, 'these are keywords')
        self.assertEqual(parsed.operator, Operator('OR'))

    def test_short_args_passing(self):
        parsed = parse_args(['-f', 'filename', '-k', 'these are keywords', '-o', 'OR'])
        self.assertEqual(parsed.file, 'filename')
        self.assertEqual(parsed.keywords, 'these are keywords')
        self.assertEqual(parsed.operator, Operator('OR'))

    def test_missing_args(self):
        with self.assertRaises(SystemExit) as ex:
            parse_args(['-some', 'nonsense'])

        self.assertEqual(ex.exception.code, 2)

        with self.assertRaises(SystemExit) as ex:
            parse_args(['--operation', 'XOR'])

        self.assertEqual(ex.exception.code, 2)

