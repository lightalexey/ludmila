from functools import lru_cache
def move(h):
    a, b=h
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2), (a, b*3)
@lru_cache(None)
def game(h):
    if sum(h)>=84:
        return 'win'
    if any(game(m)=='win' for m in move(h)):
        return 'P1'
    if any(game(m)=='P1' for m in move(h)):
        return 'V1'
    if any(game(m)=='V1' for m in move(h)):
        return 'P2'
    if all(game(m)=='P1' or game(m)=='P2' for m in move(h)):
        return 'V2'
for s in range(1, 67+1):
    if game((16, s)) is not None:
        print(s,game((16, s)))