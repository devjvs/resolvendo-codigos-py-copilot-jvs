"""Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 
Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.
"""

def verificar_par_impar():
    """Verifica se um número inteiro fornecido pelo usuário é par ou ímpar."""

    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")


if __name__ == "__main__":
    verificar_par_impar()