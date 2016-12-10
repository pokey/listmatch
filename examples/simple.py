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

nfa = concat(
    zero_or_more(atom(is_a)),
    one_or_more(
        options(
            atom(is_b),
            concat(atom(is_c), maybe(atom(is_d)))
        )
    )
)

matched = nfa.match(input)
print(matched)  # True
