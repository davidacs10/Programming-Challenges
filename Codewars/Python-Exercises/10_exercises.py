def tribonacci(signature, n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    secuencia = signature[:3]
    for _ in range(3, n):
        siguiente = sum(secuencia[-3:])
        secuencia.append(siguiente)

    return secuencia

signature = [20,21,22]
print(tribonacci(signature, 1))

def tribonacci(signature, n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    res = signature[:n]
    for _ in range(3, n): res.append(sum(res[-3:]))
    return res

signature = [20,21,22]

print(tribonacci(signature, 10))