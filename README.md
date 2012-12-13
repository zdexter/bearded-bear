bearded-bear
============

A parser combinator library for parsing ambiguous left-recursive grammars in polynomial time and space.

Built to learn more about Python's set types, memoization, and combinatorial parsing.

Background
--------

This library is based on "Parser Combinators for Ambiguous Left-Recursive Grammars" (Frost, Hafiz and Callaghan). The paper is available online here:

http://davinci.newcs.uwindsor.ca/~richard/PUBLICATIONS/PADL_08.pdf

Frost et al basically find that we can using memoization to get polynomial runtime and space efficiency for combinatorially parsing ambiguous left-recursive grammars. The authors note that Norvig found a way to achieve sub-exponential runtime for top-down parser combinators. They extend Norvig's work and find a way to do that for the grammars in question.

Motivation / options for parsing ambiguous left-recursive grammars
--------

Why not just avoid left recursion by left-factoring the grammar? It turns out that left-factoring a left-recursive grammar makes the grammar generate different parse trees! If you're doing natural language processing, this can be problematic. See page 4 of the paper for more details.

Why not use a parsing expression grammar (PEG)? PEGs cannot handle ambiguous grammars - or, more precisely, they define away ambiguity by deciding which parse trees to use. The decision process can be implicit in PEG libraries, leading to confusion and even unexpected behavior for users of PEGs.

Questions I have
--------

Is it really the case that we cannot factor out left recursion from some PEGs without "[complicating] the integration of semantic actions"? This Microsoft Research paper suggests it may be possible for many context-free natural languages grammars: http://acl.eldoc.ub.rug.nl/mirror/A/A00/A00-2033.pdf
