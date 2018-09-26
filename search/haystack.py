"""
This class performs a search in a list of given strings
"""
from enum import Enum


class Operator(Enum):
    operator_or = 'OR'
    operator_and = 'AND'

    def __str__(self):
        return self.value


class HaystackCollection:

    def __init__(self, haystacks):
        self.haystacks = haystacks

    def search(self, operation, needles):
        operation_map = {
            Operator('OR'): any,
            Operator('AND'): all,
        }
        # we do not need to validate whether operation is valid or not because enum takes care of it
        filter_callable = operation_map[operation]
        return [index for index, haystack in enumerate(self.haystacks)
                if filter_callable(needle in haystack.split() for needle in needles)]
