"optimize with linear-time scans using dictionaries"

import set
                                           # fastset.Set extends set.Set
class Set(set.Set):
    def __init__(self, value = []):
        self.data = {}                     # manages a local dictionary
        self.concat(value)                 # hashing: linear search times

    def intersect(self, other):
        res = {}
        for x in other:                    # other: a sequence or Set
            if x in self.data:             # use hash-table lookup; 3.X
                res[x] = None
        return Set(res.keys())             # a new dictionary-based Set

    def union(self, other):
        res = {}                           # other: a sequence or Set
        for x in other:                    # scan each set just once
            res[x] = None
        for x in self.data.keys():         # '&' and '|' come back here
            res[x] = None                  # so they make new fastset's
        return Set(res.keys())

    def concat(self, value):
        for x in value: self.data[x] = None

    # inherit and, or, len
    def __getitem__(self, ix):  
        return list(self.data.keys())[ix]            # 3.X: list()

    def __repr__(self):           
        return '<Set:%r>' % list(self.data.keys())  # ditto


'''
One way to optimize set performance is by changing the implementation to use dictionaries
rather than lists for storing sets internally—items may be stored as the keys of a dictionary whose values are all None. Because lookup time is constant and short for
dictionaries, the in list scans of the original set can be replaced with direct dictionary
fetches in this scheme.
'''


"""
In traditional terms, moving sets to dictionaries replaces slow
linear searches with fast hashtable fetches. A computer scientist would explain this by
saying that the repeated nested scanning of the list-based intersection is an exponential
algorithm in terms of its complexity, but dictionaries can be linear.
"""


'''
This works about the same as the previous version, even though the internal implementation
is radically different:
>>> from fastset import Set
>>> users1 = Set(['Bob', 'Emily', 'Howard', 'Peeper'])
>>> users2 = Set(['Jerry', 'Howard', 'Carol'])
>>> users3 = Set(['Emily', 'Carol'])
>>> users1 & users2
<Set:['Howard']>
>>> users1 | users2
<Set:['Howard', 'Peeper', 'Jerry', 'Carol', 'Bob', 'Emily']>
>>> users1 | users2 & users3
<Set:['Peeper', 'Carol', 'Howard', 'Bob', 'Emily']>
>>> (users1 | users2) & users3
<Set:['Carol', 'Emily']>
>>> users1.data
{'Peeper': None, 'Bob': None, 'Howard': None, 'Emily': None}
'''