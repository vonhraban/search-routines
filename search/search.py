"""
This class performs a search in a list of given strings
"""


class StringSearch():

    def __init__(self, haystacks):
        self.haystacks = haystacks

    def find_indices_containing_all_of(self, needles):
        return [index for index, haystack in enumerate(self.haystacks)
                if all(needle in haystack.split() for needle in needles)]

    def find_indices_containing_any_of(self, needles):
        return [index for index, haystack in enumerate(self.haystacks)
                if any(needle in haystack.split() for needle in needles)]
