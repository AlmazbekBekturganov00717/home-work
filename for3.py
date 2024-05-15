def power(A, N):
    result = 1
    for _ in range(N):
        result *= A
    return result

A = 2.5
N = 4
print("A в степени N равно:", power(A, N))
# тут как я понял просто надо умножить число А на N несколько раз и также использовать цикл
