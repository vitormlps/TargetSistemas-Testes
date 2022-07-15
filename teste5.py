# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;


import unittest

# Realiza testes unitários para verificar se a função está funcionando.
class TestStringMethods(unittest.TestCase):
    # Testa se função está executando conforme esperado.
    def test_reverse_string(self):
        raw_string = "Caracteres invertidos."
        self.assertEqual(reverse_string(raw_string), ".soditrevni seretcaraC")

    # Testa duas execuções sequenciais da função para verificar
    # se a string volta e continua igual a original.
    def test_reverse_input(self):
        raw_string = "Se vai, volta."
        self.assertEqual(reverse_string(reverse_string(raw_string)), raw_string)


# Inverte a string informada, caracter por caracter.
def reverse_string(raw_string: str):
    if len(raw_string) <= 1:
        return raw_string
    return reverse_string(raw_string[1:]) + raw_string[0]


# Chamada dos testes unitários.
if __name__ == "__main__":
    unittest.main()
