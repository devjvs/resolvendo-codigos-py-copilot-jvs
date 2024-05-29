# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def repetir_string():
    """Solicita uma string e um número inteiro, e retorna a string repetida o número de vezes informado."""

    texto = input("Digite uma string: ")
    while True:
        try:
            repeticoes = int(input("Digite um número inteiro: "))
            if repeticoes >= 0:  # Garante que o número seja não negativo
                break
            else:
                print("Por favor, digite um número inteiro não negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    string_repetida = texto * repeticoes
    print("String repetida:", string_repetida)

if __name__ == "__main__":
    repetir_string()
