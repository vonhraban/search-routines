"""
    Accepted types of search:
    AND - all of the given keywords must exists in the string
    OR - one or more keywords must exist in the string
"""
import argparse
import sys
from search.haystack import HaystackCollection, Operator


def parse_args(cli_args):
    parser = argparse.ArgumentParser(description='Perform a keyword search query against a file.')
    parser.add_argument('-k', '--keywords', type=str,
                        required=True, help='Space separated keywords to search for')
    parser.add_argument('-o', '--operator', type=Operator, choices=list(Operator),
                        required=True, help='Operator: AND means all keywords have to present, OR means any')
    parser.add_argument('-f', '--file', type=str,
                        required=True, help='Source file to search against')
    return parser.parse_args(cli_args)


if __name__ == "__main__":
    parsed_args = parse_args(sys.argv[1:])
    try:
        with open(parsed_args.file) as f:
            content = f.readlines()
    except EnvironmentError:
        print("Could not read file %s" % parsed_args.file)
        sys.exit(1)

    haystacks = HaystackCollection(content)
    print(
        ",".join(
            map(
                str,
                haystacks.search(parsed_args.operator, parsed_args.keywords.split())
            )
        )
    )
