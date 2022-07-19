import re
import pprint

from direction import Direction
from move import Move


class Parser:
    class State:
        def __init__(self, text, symbol):
            self.remainder = text.strip()
            self.tree = {symbol: []}

        def __str__(self):
            return '{} {}'.format('PARSED OK' if not self.remainder else self.remainder, self.tree)

    class Result:
        def __init__(self, tree):
            self.tree = tree

        def find_symbols(self, symbol, root=None, do_flatten=True):
            matches = []

            def flatten(v):
                if type(v) == list:
                    if len(v) == 0:
                        return None
                    elif len(v) == 1:
                        return v[0]

                return v

            def search(o):
                if type(o) == list:
                    [search(item) for item in o]

                elif type(o) == dict:
                    for k, v in o.items():
                        if k == symbol:
                            matches.append(flatten(v))
                        else:
                            search(v)
                else:
                    return

            search(root or self.tree)

            return flatten(matches) if do_flatten else matches

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
        consume_result = self._consume(text, 'START')
        if not consume_result.remainder:
            return Parser.Result(consume_result.tree)
        raise ValueError('Unable to parse "{}" failed near character {}'.format(text, len(text) - len(consume_result.remainder)+1))


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

def to_moves(result):
    def get_count_from_angle(angle):
        if angle == "2":
            return 2
        elif angle == "'":
            return -1
        elif angle is None:
            return 1

        raise ValueError('Unknown angle value: {}'.format(angle))

    def to_move(step):
        single_layer_turn = result.find_symbols('SINGLE_LAYER_TURN', step)
        if single_layer_turn:
            layer = int(result.find_symbols('SINGLE_LAYER', single_layer_turn) or 1)
            face = Direction(result.find_symbols('FACE_UPPER', single_layer_turn))
            angle = get_count_from_angle(result.find_symbols('ANGLE', single_layer_turn))
            return Move([layer], face, angle)

    return [to_move(step) for step in result.find_symbols('STEP', do_flatten=False)]

print(r.tree)
# pp = pprint.PrettyPrinter(indent=4)
# for step in r.find_symbols('STEP'):
#     print(step)
#     s = r.find_symbols('SINGLE_LAYER_TURN', step)
#     if s:
#         print('s',r.find_symbols('SINGLE_LAYER', s), r.find_symbols('FACE_UPPER', s), r.find_symbols('ANGLE', s))
#     m = r.find_symbols('MULTI_LAYER_TURN', step)
#     if m:
#         print('m',r.find_symbols('MULTI_LAYER', m), r.find_symbols('FACE_LOWER', m), r.find_symbols('ANGLE', m))
# # pp.pprint(r.find_symbols('STEP'))
print(to_moves(r))


