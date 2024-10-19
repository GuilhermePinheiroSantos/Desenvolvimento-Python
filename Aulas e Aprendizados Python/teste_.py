import random
import numpy as np
import matplotlib.pyplot as plt

def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1
    passos = 0

    while inicio <= fim:
        passos += 1
        meio = (inicio + fim) // 2
        palpite = lista[meio]

        if palpite == item:
            return meio, passos
        if palpite < item:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1, passos




tamanhos = [10, 25, 50, 75, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000]
resultados = {}

for tamanho in tamanhos:
    lista = sorted(random.sample(range(1, 2 * tamanho), tamanho))
    item_procurado = max(lista) + 1

    _, passos = busca_binaria(lista, item_procurado)
    resultados[tamanho] = passos

tamanhos = list(resultados.keys())
passos = list(resultados.values())

plt.figure(figsize=(10, 6))
plt.plot(tamanhos, passos, marker='o', label='Passos')

log_tamanhos = np.log(tamanhos)
coeficientes = np.polyfit(log_tamanhos, passos, 1)
polinomio = np.poly1d(coeficientes)

x_fit = np.linspace(min(log_tamanhos), max(log_tamanhos), 100)
y_fit = polinomio(x_fit)

plt.plot(np.exp(x_fit), y_fit, color='red', linestyle='--', label='log2(n)')

plt.xscale('linear')
plt.yscale('linear')
plt.xlabel('Tamanho da lista (n)')
plt.ylabel('Número de passos')
plt.title('Análise da Busca Binária')
plt.legend()
plt.grid(True)
plt.show()