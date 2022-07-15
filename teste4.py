# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

# Limpa dados informados e os adiciona a um dicionário.
def limpar_dados(faturamento_mensal: dict):
    dados = """SP – R$67.836,43
    RJ – R$36.678,66
    MG – R$29.229,88
    ES – R$27.165,48
    Outros – R$19.849,53"""

    sem_espaco = dados.replace(" ", "")
    sem_ponto_milhar = sem_espaco.replace(".", "")
    estilo_float = sem_ponto_milhar.replace(",", ".")
    estilo_dict = estilo_float.replace("–R$", ":")
    dados_limpos = estilo_dict.split("\n")

    for fatur_estado in dados_limpos:
        temp = fatur_estado.partition(":")
        faturamento_mensal.setdefault(temp[0], float(temp[2]))


# Calcula e apresenta na tela o percentual de cada estado referente ao valor total mensal.
def representacao_percentual_mensal():
    faturamento_mensal: dict = {}
    limpar_dados(faturamento_mensal)

    total_mensal = sum(faturamento_mensal.values())

    for estado, valor in faturamento_mensal.items():
        percentual = (valor / total_mensal) * 100
        print(f"{estado} representa {percentual:.2f}% do total.")


# Chamada da função principal.
representacao_percentual_mensal()
