import numpy as np
import matplotlib.pyplot as plt


'''
ENUNCIADO:

O objetivo deste exercício é implementar duas abordagens para calcular a sequência de Fibonacci: 
uma abordagem recursiva e outra iterativa. Em seguida, você irá avaliar empiricamente a complexidade de cada algoritmo, 
contando o número de iterações ou chamadas realizadas durante a execução.
''' 
'''
1)
Implemente a função fibonacci_recursivo(n), que retorna o n-ésimo número de Fibonacci usando a abordagem recursiva.
A função deve também contar e retornar o número de chamadas feitas durante o cálculo.
'''

def fib_recursiva(n):
    global interacao
    interacao += 1
    if n == 1:
        return 0 
    elif n == 2:
        return 1 
    else:
        return fib_recursiva(n - 1) + fib_recursiva(n - 2)

interacao = 0
print('Valor da sequência de Fibonacci : ', fib_recursiva(1))
print('Interações: ', interacao)


'''
2)
Implemente a função fibonacci_iterativo(n), que retorna o n-ésimo número de Fibonacci usando a abordagem iterativa.
A função deve também contar e retornar o número de iterações realizadas durante o cálculo.
'''

def fib_iterativa(f):
    if f == 1:
        return 0, 0 #fibonacci(0) = 1 , 0 interações
    elif f == 2:
        return 1, 0 #fibonacci(2) = 1 , 0 interações
    
    a, b = 0, 1 #Representa fibonacci(1) e fibonacci(2)
    contador = 0

    for i in range(3, f + 1):
        a, b = b , a + b
        contador += 1
    return b, contador

f = 10 # valor qualquer
resultado, contador = fib_iterativa(f)
print('Valor da sequência de fibonacci : ', resultado)
print('interações: ', contador)

'''
3)
No programa principal, teste ambas as funções para valores de  n variando de 1 a 10 (ou um intervalo maior se preferir) 
e armazene o número de iterações/chamadas realizadas para cada valor de n em um dicionário com o seguinte formato:
{n: qtde de iterações/chamadas}
'''
resultados = {}

for n in range (1 , 11):

    interacao = 0
    fib_recursiva(n)

    resultados[n] = {
        'recursiva': interacao,
        'iterativa': fib_iterativa(n)[1]  
    }

for n, valores in resultados.items():
    print(f"n: {n}, Chamadas Recursivas: {valores['recursiva']}, Iterações Iterativas: {valores['iterativa']}")

'''
4)
Use a biblioteca matplotlib para plotar gráficos que representem a relação entre n e o número de iterações/chamadas para ambas as abordagens. 
No gráfico, o eixo x deve representar o valor de n e o eixo y deve representar o número de iterações/chamadas.
Veja o exemplo de código anexado na aula 15 se necessário.
'''
# Extraindo os valores para o gráfico
n_values = list(resultados.keys())
recursiva_calls = [valores['recursiva'] for valores in resultados.values()]
iterativa_iterations = [valores['iterativa'] for valores in resultados.values()]

# Criando o gráfico
plt.figure(figsize=(10, 6))

# Plotando as chamadas recursivas
plt.plot(n_values, recursiva_calls, label='Chamadas Recursivas', marker='o', color='blue')
# Plotando as iterações iterativas
plt.plot(n_values, iterativa_iterations, label='Iterações Iterativas', marker='o', color='red')

# Configurando o gráfico
plt.title('Relação entre n e o Número de Chamadas/Iterações')
plt.xlabel('n')
plt.ylabel('Número de Chamadas/Iterações')
plt.xticks(n_values)  # Definindo os ticks do eixo x
plt.grid()
plt.legend()
plt.tight_layout()

# Exibindo o gráfico
plt.show()

'''
5)
Pesquise pela complexidade teórica das funções e compare os resultados obtidos. 
Discuta como o número de iterações ou chamadas muda à medida que n aumenta e como isso reflete na complexidade dos algoritmos.
'''
"""
ELABORADO EM ARQUIVO DOC
"""






'''
6)
Aplique a técnica de memoização à função recursiva e analise novamente a complexidade. Discuta a respeito do resultado obtido.
'''
def fib_recursiva_memo(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        memo[n] = fib_recursiva_memo(n - 1, memo) + fib_recursiva_memo(n - 2, memo)
        return memo[n]

'''
EXPLICAÇÃO EM ARQUIVO DOC
'''