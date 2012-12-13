def read_file(filename):
    """Return unparsed ruleset."""
    f = open(filename, 'r')
    rules = f.readlines()
    return rules

def get_rule_dict(rules):
    """
    >>> gen("s ::= np vp | s pp")
    {'s': 'np vp | s pp'}
    >>> gen('noun ::= "i" | "man" | "park" | "bat"')
    {'noun': '"i" | "man" | "park" | "bat"'}
    """
    rules = map(lambda x: x.strip(), rules.split("::="))
    rules = dict([(rules[i], rules[i+1]) for i in range(len(rules) / 2)])
    return rules

def combinate(rule_dict):
    """Return a callable combinatorial parser for the grammar
        represented by rule_dict.
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
