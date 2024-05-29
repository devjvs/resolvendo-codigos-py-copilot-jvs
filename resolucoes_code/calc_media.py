# Agora vamos calcular a média de três notas fornecidas na entrada do usuário. 

def calcular_media():
    """Calcula a média de três notas fornecidas pelo usuário."""

    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Digite a nota {i + 1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")

    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media:.2f}")  # Formata para duas casas decimais


if __name__ == "__main__":
    calcular_media()