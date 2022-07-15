# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

# Lê arquivo e transforma os dados em um dicionário.
def ler_arquivo():
    data: dict = {}

    with open("dados.json", "r") as dados:
        vetor = json.load(dados)
        dados.close()

        for linha in vetor:
            data.setdefault(linha["dia"], linha["valor"])

    return data


# Analisa faturamentos diários do mês, calculando mínimo e máximo faturado em um dia e a quantidade de dias nos quais o faturamento foi superior à média.
def analise_mensal():
    faturamento_diario: dict = ler_arquivo()
    faturamento_dias_uteis = faturamento_diario.copy()
    superior_a_media = 0

    for dia, faturamento in faturamento_diario.items():
        if faturamento <= 0:
            faturamento_dias_uteis.pop(dia)
        if faturamento > (
            sum(faturamento_dias_uteis.values()) / len(faturamento_dias_uteis)
        ):
            superior_a_media += 1

    return (
        min(faturamento_diario.values()),
        min(faturamento_dias_uteis.values()),
        max(faturamento_diario.values()),
        superior_a_media,
    )


# Apresenta análise na tela, arredondando valores para 2 casas decimais.
def print_analise():
    min_fatur, min_fatur_dias_uteis, max_fatur, num_dias = analise_mensal()
    print(
        f"""
Menor valor de faturamento diário: R${min_fatur:.2f}
Menor valor de faturamento em dias úteis: R${min_fatur_dias_uteis:.2f}
Maior valor de faturamento diário: R${max_fatur:.2f}
Número de dias nos quais o faturamento foi superior à média mensal: {num_dias} dias"""
    )


# Chamada da função de apresentação.
print_analise()
