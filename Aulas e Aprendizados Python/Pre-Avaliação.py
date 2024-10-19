import random

# Declaração de função
def gerar_cpf():
    return "".join([str(random.randint(0, 9)) for _ in range(9)])


def gerar_subconjunto(conjunto):
    return set(random.sample(list(conjunto), int(random.random() * 100)))


# Conjunto nulo
conjunto_pessoas = set()

# Loop do programa
while len(conjunto_pessoas) < 100:
    cpf = gerar_cpf()
    conjunto_pessoas.add(cpf)

# Declaração dos subconjuntos
esportes = {
    "surfe": gerar_subconjunto(conjunto_pessoas),
    "volei": gerar_subconjunto(conjunto_pessoas),
    "ginastica": gerar_subconjunto(conjunto_pessoas),
    "judo": gerar_subconjunto(conjunto_pessoas),
}
"""
Calcule a probabilidade de que uma pessoa sorteada aleatoriamente tenha assistido:
Judô ou surfe
Pelo menos dois esportes
Todos os esportes
Nenhum esporte
"""

# Probabilidade de judo ou surfe
uniao_judo_surfe = esportes["judo"] | esportes["surfe"]
quantidade_uniao_judo_surfe = len(uniao_judo_surfe)

print(
    f"A probabilidade de uma pessoa sorteada aleatoriamente tenha assistido judô ou surfe é de: {round((quantidade_uniao_judo_surfe/100)*100)}%"
)


# Probabilidade de pelo menos dois esportes
judo_volei = esportes["judo"] & esportes["volei"]
judo_ginastica = esportes["judo"] & esportes["ginastica"]
judo_surfe = esportes["judo"] & esportes["surfe"]
volei_ginastica = esportes["volei"] & esportes["ginastica"]
volei_surfe = esportes["volei"] & esportes["surfe"]
ginastica_surfe = esportes["ginastica"] & esportes["surfe"]

pelo_menos_dois = (
    judo_volei
    | judo_ginastica
    | judo_surfe
    | volei_ginastica
    | volei_surfe
    | ginastica_surfe
)

quantidade_pelo_menos_dois = len(pelo_menos_dois)
print(
    f"\nA probabilidade de uma pessoa sorteada aleatoriamente tenha assistido pelo menos dois esportes é de: {round((quantidade_pelo_menos_dois/100)*100)}%"
)

# Probabilidade de todos os esportes
uniao = esportes["judo"] & esportes["surfe"] & esportes["ginastica"] & esportes["volei"]
quantidade_uniao = len(uniao)

print(
    f"\nA probabilidade de uma pessoa sorteada aleatoriamente tenha assistido todos esportes é de: {round((quantidade_uniao/100)*100)}%"
)

# Probabilidade de nenhum esporte
assistiram_algum_esporte = (
    esportes["judo"] | esportes["volei"] | esportes["ginastica"] | esportes["surfe"]
)
nenhum_esporte = conjunto_pessoas - assistiram_algum_esporte
quantidade_nenhum_esporte = len(nenhum_esporte)

print(
    f"\nA probabilidade de uma pessoa sorteada aleatoriamente não ter assistido a nenhum esporte é de: {round((quantidade_nenhum_esporte/100)*100)}%"
)
