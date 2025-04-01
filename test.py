from main  import *
Aaa = [1, 2, 3, 4]

print(Aaa)
print(is_trasition(Aaa, make_reflection(Aaa)))
print(f'gol {make_simmetric(Aaa)}')

A = [1, 2, 3]
R1 = [(1, 1), (2, 2), (3, 3)] # Для двух видов рефлексивности
R2 = [(1, 2), (2, 1)] # Для симметричности
R3 = [(1, 1), (2, 2)] # Для асимметричности

print(f'Test 1 {is_reflection(A, R1)}')
print(f'Test 2 {is_simmetric(A, R1)}')
print(f'Test 3 {is_trasition(A, R1)}')

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