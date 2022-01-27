#! /usr/bin/env python3

import chess.pgn
import pandas as pd
from collections import defaultdict


def convert(header):
    res, white, black = header.get('Result'), header.get('White'), header.get('Black')
    if res == "*":
        return ((white, '*'), (black, '*'))
    if res == '1/2-1/2':
        return ((white, 0.5), (black, 0.5))
    return ((white, int(res[0])), (black, int(res[-1])))


headers = []
with open("lichess_broadcast_tata-steel-masters-2022_IsMvGXWN_2022.01.26.pgn") as pgn:
    for header in iter(lambda: chess.pgn.read_headers(pgn), None):
        headers.append(header)

table = defaultdict(dict)
totals = defaultdict(int)

for header in headers:
    ((wn, ws), (bn, bs)) = convert(header)
    table[wn][bn] = ws
    table[bn][wn] = bs
    if ws != '*':
        totals[wn] += ws
        totals[bn] += bs

sortedtotals = sorted(totals.items(), key=lambda item: item[1], reverse=True)

output = {p: [] for p, s in sortedtotals}

for player in output:
    for opp in output:
        res = table[player].get(opp)
        if res or res == 0:
            output[player].append(res)
        else:
            output[player].append('-')

for player in output:
    output[player].append(totals[player])

df = pd.DataFrame.from_dict(output).transpose()
df.rename(columns={x: x + 1 for x in df.columns}, inplace=True)
df.rename(columns={df.columns[-1]: 'Total'}, inplace=True)
df.to_markdown(buf="standings")
