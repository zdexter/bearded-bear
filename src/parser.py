def lex(s):
    """Return a list of tokens."""
    return s.split(" ");

# j is the index we want to match

def rec_type(j, the_type):
    def _(token_list):
        """Return index of next token if match.
            Otherwise, return the empty set.
        """
        if j < len(token_list):
            if type(token_list[j]) is the_type:
                return set([j+1])
            return set()
        raise Exception('Cannot recognize integer past end of input')
    return _

def rec_int(j):
    """
    >>> rec_int(0)([1, 2, 3, 4])
    set([1])
    >>> rec_int(3)([5, 6, 7, 8])
    set([4])
    """
    return rec_type(j, int)
def rec_str(j):
    """
    >>> rec_str(0)(["lol"])
    set([1])
    >>> rec_str(2)(["lol", "that", "rofl", "copter", "lol"])
    set([3])
    """
    return rec_type(j, str)

def alt(j, *recs):
    """
    >>> alt(1, rec_int, rec_str)(["lol", 127, "copter", 128])
    set([2])
    """
    def _(token_list):
        """Return union of applying each recognizer to index j of the input."""
        # Destructure each recognizer into a set
        return set.union(*[rec(j)(token_list) for rec in recs])
    return _

def comp(j, p, q): # Composite, or sequence, recognizer
    """
    >>> comp(0, rec_str, rec_str)(["lol", "copter"])
    set([2])
    >>> comp(0, rec_str, rec_int)(["lol", 1, "copter"])
    set([2])
    >>> comp(0, rec_str, rec_str)([1, 2, 3])
    set([])
    >>> comp(0, rec_int, rec_str)(["lol", 1])
    set([])
    """
    def _(token_list):
        """Apply p to input; return union of applying q to that output."""
        p_out = p(j)(token_list)
        out = set()
        for i in p_out:
            out = out.union(q(i)(token_list))
        return out
    return _

memo_table = {} # Position: (Parser function name, result set)

def memoize(j):
    def _(parser, *args)
        """Return result set for parser(j) if it's memoized.
           Else, memoize result set and return it.
        """
        stored_set = getattr(memo_table[j], False)
        if stored_set[0] == parser.__name__:
            return stored_set[1]
        memo_table[j] = parser(j, args)
        return memo_table[j]
    return _

def parse(token_list):
    """Perform syntactic analysis on input."""
    pass

if __name__ == '__main__':
    s = "1 5 0 3 92 91 109 8 3"
    #parse(s)
    #print recognize()(3)
    import doctest
    doctest.testmod()
