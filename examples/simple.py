from listmatch import (
    concat,
    options,
    zero_or_more,
    one_or_more,
    maybe,
    atom
)

input = ['a', 'a', 'b', 'c', 'c', 'd']


def is_a(c):
    return c == 'a'


def is_b(c):
    return c == 'b'


def is_c(c):
    return c == 'c'


def is_d(c):
    return c == 'd'

# The following NFAs are equivalent
nfa1 = zero_or_more('a') + one_or_more('b' | ('c' + maybe('d')))
nfa2 = zero_or_more(is_a) + one_or_more(is_b | (is_c + maybe(is_d)))
nfa3 = concat(
    zero_or_more(atom(is_a)),
    one_or_more(
        options(
            atom(is_b),
            concat(atom(is_c), maybe(atom(is_d)))
        )
    )
)

if nfa1.match(input):
    print("First matched!")

if nfa2.match(input):
    print("Second matched!")

if nfa3.match(input):
    print("Third matched!")
