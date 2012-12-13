def lex(s):
    """Return a list of tokens."""
    return s.split(" ");

def rec_int(j):
    """
    >>> rec_int(0)([1, 2, 3, 4])
    set([1])
    >>> rec_int(3)([5, 6, 7, 8])
    set([4])
    """
    def _(token_list):
        """Return index of next token if match.
            Otherwise, return the empty set.
        """
        if j < len(token_list):
            if type(token_list[j]) is int:
                return set([j+1])
            return set()
        raise Exception('Cannot recognize integer past end of input')
    return _

def alt(j, *recs):
    """Return a method that will return indicies of each distinct
        recognized elements in the input sets.
    >>> alt(1, rec_int, rec_int)(["lol", 127, "copter", 128])
    set([2])
    """
    def _(token_list):
        # Destructure each recognizer into a set
        return set.union(*[rec(j)(token_list) for rec in recs])
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
