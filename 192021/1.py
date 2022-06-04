# За один ход игрок может добавить в одну из куч (по своему выбору) один камень
# или увеличить количество камней в куче в два раза.
# В начальный момент в первой куче было семь камней, во второй куче— S камней;
# 1≤S≤69.
# Игра завершается в тот момент,
# когда суммарное количество камней в кучах становится не менее 77.
from functools import lru_cache
def move(h):
    a, b = h
    return (a+1, b), (a, b + 1), (a * 2, b), (a, b * 2)
@lru_cache(None)
def game(h):
    if sum(h) >= 77:
        return 'win'
    if any(game(m) == 'win' for m in move(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in move(h)): # поменять на any Для 19 задания, Ваня первым ходом при неудачном ходе Пети.
        return 'V1'
    if any(game(m) == 'V1' for m in move(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m)=='P2' for m in move(h)):
        return 'V2'

for s in range(1, 69 + 1):
    if game((7, s)) is not None:
        print(s, game((7, s)))
