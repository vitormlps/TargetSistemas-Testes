# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence
# ou não a sequência.

# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

# Executa fibonacci com memorização das posições já calculadas. Assim é mais rápido que processar somando para posições maiores.
def fib(num: int, memo: dict):
    if num in memo:
        return memo[num]
    if num <= 2:
        return 1
    memo[num] = fib(num - 1, memo) + fib(num - 2, memo)
    return memo[num]


# Aproveitando a memória, verifica se o número informado faz parte da sequência ou não.
def isInFib(num: int):
    memo: dict = {}
    fib(num, memo)
    print(memo)
    if num not in memo.values():
        print("Isn't in Fibonacci!")
    else:
        print("Is in Fibonacci!")


# Chama a função principal com o número informado.
isInFib(8)
