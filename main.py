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