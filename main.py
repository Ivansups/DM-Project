from tkinter.filedialog import FileDialog
from itertools import *

def is_reflection(A, R): # Рефлексивность
    for x in A:
        if (x, x) not in R:
            return False
    return True

def is_simmetric(A, R): # Симметричность
    for (x, y) in R:
        if (y, x) not in R:
            return False
    return True

def is_asimetric(R): # Антисимметричность
    for (x, y) in R:
        if x != y and (x, y) in R and (y, x) not in R:
            return False
    return True

def is_trasition(A, R): # Транзитивость
    for (x, y) in R:
        for (y2, z) in R:
            if y2 != y or (x, z) not in R:
                return False
    return True

def is_equivalent(A, R): # Проверка отношения на эквивалентность
    if is_reflection(A, R) and is_simmetric(A, R) and is_trasition(A, R) and is_trasition2(A, R):
        return True

def is_partial_order(A, R): # Проверка отношения на частичный порядок
    if is_reflection(A, R) and is_asimetric(R) and is_trasition(A, R):
        return True

def make_reflection(A):
    answ = []
    for x in A:
        answ.append((x, x))
    return answ

# def make_trasition(A):
#     answ = []
#     indX = 0
#     indY = 1
#     indZ = 2
#     for x in range(indZ, len(A)):
#         answ.append((A[indX], A[indY]))
#         answ.append((A[indY], A[indZ]))
#         answ.append((A[indX], A[indZ]))
#         if x == len(A):
#             x = indY
#     return set(answ)

def make_simmetric(A):
    answ = []
    answ.append((A[0], A[-1]))
    answ.append((A[-1], A[0]))
    for x in range(1, len(A)):
        answ.append((A[x - 1], A[x]))
        answ.append((A[x], A[x - 1]))
    return answ

Aaa = [1, 2, 3, 4]

print(Aaa)
print(is_trasition(Aaa, make_reflection(Aaa)))
print(f'gol {make_simmetric(Aaa)}')
print(f'gol {make_trasition(Aaa)}')


A = [1, 2, 3]
R1 = [(1, 1), (2, 2), (3, 3)] # Для двух видов рефлексивности
R2 = [(1, 2), (2, 1)] # Для симметричности
R3 = [(1, 1), (2, 2)] # Для асимметричности

print(f'da {is_reflection(A, R1)}')
print(f'da {is_simmetric(A, R1)}')
print(f'da {is_trasition(A, R1)}')

AT = [1, 2, 3]
RT = [(1, 2), (1, 3), (3, 3), (2, 3), (2, 2)]

e = ["a", "b", "c", "d", "e"]
d2 = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]
d3 = [('a', 'b'), ('b', 'c'), ('a', 'c'), ('b', 'd'), ('c', 'd'), ('d', 'e'), ('c', 'e'), ('a', 'e'), ('b', 'e'), ('a', 'd')]
d4 = []

print(f'Это тест рефлексивности ---> {is_reflection(A, R1)}')
print()
print(f'Это тест симметричности ---> {is_simmetric(A, R2)}')
print()
print(f'Это тест аисметричности ---> {is_asimetric(R3)}')
print()
print(f'Это тест транзитивности ---> {is_trasition(AT, RT)}')
print()
print(f't1 {is_simmetric(e, d4)}')
print(f't2 {is_trasition(e, d4)}')
print(f't3 {is_reflection(e, d4)}')

# print(is_reflection(e, d))
# print(is_simmetric(e, d))
# print(is_asimetric(d))
# print(is_trasition(e, d))

#Диаграмма Хассе