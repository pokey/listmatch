# -*- coding: utf-8 -*-
from listmatch.util import pairwise


class State:
    def __init__(self):
        self.epsilon = []  # epsilon-closure
        self.matcher = lambda x: False
        self.next_state = None
        self.is_end = False


class NFA:
    def __init__(self, start, end):
        # start and end states
        self.start = start
        self.end = end
        end.is_end = True

    def addstate(self, state, state_set):
        """
        add state + recursively add epsilon transitions
        """
        if state in state_set:
            return
        state_set.add(state)
        for eps in state.epsilon:
            self.addstate(eps, state_set)

    def match(self, l):
        current_states = set()
        self.addstate(self.start, current_states)

        for e in l:
            next_states = set()
            for state in current_states:
                if state.matcher(e):
                    trans_state = state.next_state
                    self.addstate(trans_state, next_states)

            current_states = next_states

        for s in current_states:
            if s.is_end:
                return True
        return False


def atom(matcher):
    s0 = State()
    s1 = State()
    s0.matcher = matcher
    s0.next_state = s1
    return NFA(s0, s1)


def concat(*args):
    if len(args) == 0:
        s0 = State()
        return NFA(s0, s0)
    if len(args) == 1:
        return args[0]
    for n1, n2 in pairwise(args):
        n1.end.is_end = False
        n1.end.epsilon.append(n2.start)
    return NFA(args[0].start, args[-1].end)


def options(*args):
    s0 = State()
    s0.epsilon = [nfa.start for nfa in args]
    s3 = State()
    for nfa in args:
        nfa.end.epsilon.append(s3)
        nfa.end.is_end = False
    return NFA(s0, s3)


def _rep(n1, at_least_once):
    s0 = State()
    s1 = State()
    s0.epsilon = [n1.start]
    if not at_least_once:
        s0.epsilon.append(s1)
    n1.end.epsilon.extend([s1, n1.start])
    n1.end.is_end = False
    return NFA(s0, s1)


def zero_or_more(n1):
    return _rep(n1, at_least_once=False)


def one_or_more(n1):
    return _rep(n1, at_least_once=False)


def maybe(n1):
    n1.start.epsilon.append(n1.end)
    return n1
