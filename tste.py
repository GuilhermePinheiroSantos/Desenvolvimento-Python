from memory_profiler import profile

# Utilizando um dicionário para memoização
memo = {}

@profile
def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

def profile_fibonacci():
    n = 20
    result = fibonacci(n)
    print(f"Resultado: {result}")

profile_fibonacci()