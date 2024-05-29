""" Vamos testar se uma palavra é um palíndromo?! 
Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original."""

def verificar_palindromo():
    """Verifica se uma palavra ou frase é um palíndromo."""

    texto = input("Digite uma palavra ou frase: ").lower().replace(" ", "")

    if texto == texto[::-1]:
        print(f"'{texto}' é um palíndromo!")
    else:
        print(f"'{texto}' não é um palíndromo.")


if __name__ == "__main__":
    verificar_palindromo()