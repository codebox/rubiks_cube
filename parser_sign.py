import re
import pprint


class Parser:
    class State:
        def __init__(self, text, symbol):
            self.remainder = text.strip()
            self.tree = {symbol: []}

        def __str__(self):
            return '{} {}'.format('PARSED OK' if not self.remainder else self.remainder, self.tree)

    class Result:
        def __init__(self, state):
            self.state = state

        def find_symbols(self, symbol):
            matches = []
            def search(d):
                for k,v in d.items():
                    if k == symbol:
                        matches.append(v)
                    else:
                        for item in v:
                            search(item)
            search(self.state.tree)
            return matches

    def __init__(self, grammar):
        self.rules = self._build_rules(grammar)

    def _build_rules(self, grammar):
        symbol_map = dict((s.strip() for s in rule.split('->')) for rule in grammar.strip().split('\n'))
        return {symbol: [a.strip().split() for a in alternatives.split('|')] for symbol, alternatives in symbol_map.items()}

    def _part_ok(self, symbol, part, state):
        if part == '':
            state.tree[symbol].append('')
            return True

        if part in self.rules:
            result = self._consume(state.remainder, part)
            if result:
                state.remainder = result.remainder.strip()
                state.tree[symbol].append(result.tree)
                return True
            else:
                return False

        m = re.match("^" + part, state.remainder)
        if m:
            state.remainder = state.remainder[len(m.group()):]
            state.tree[symbol].append(m.group())
            return True

        return False

    def _consume(self, text, symbol):
        matches = []

        for alternative in self.rules[symbol]:
            state = Parser.State(text, symbol)

            if all(self._part_ok(symbol, part, state) for part in alternative):
                matches.append(state)

        if len(matches):
            return sorted(matches, key=lambda m: len(m.remainder))[0]

    def parse(self, text):
        return Parser.Result(self._consume(text, 'START'))


# see https://mzrg.com/rubik/nota.shtml
grammar = '''
START -> STEPS
STEPS -> | STEP STEPS
STEP  -> SINGLE_LAYER_TURN | MULTI_LAYER_TURN | WHOLE_CUBE_ROTATION
SINGLE_LAYER_TURN -> SINGLE_LAYER FACE_UPPER ANGLE
MULTI_LAYER_TURN -> MULTI_LAYERS FACE_LOWER ANGLE
WHOLE_CUBE_ROTATION -> WHOLE_CUBE_AXIS ANGLE
WHOLE_CUBE_AXIS -> x | y | z
ANGLE -> | ' | 2
SINGLE_LAYER -> | [2-9] | [1-9][0-9]+
MULTI_LAYERS -> | MULTI_LAYER | MULTI_LAYER_RANGE
MULTI_LAYER -> [3-9] | [1-9][0-9]+
MULTI_LAYER_RANGE -> MULTI_LAYER - MULTI_LAYER
FACE_UPPER -> F | B | L | R | U | D
FACE_LOWER -> f | b | l | r | u | d
'''

p = Parser(grammar)
r=p.parse("R2 R' 5R' 3-4r")
pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(r.tree)
pp.pprint(r.find_symbols('STEP'))


