# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def calculadora_simples():
    """Solicita dois números ao usuário e realiza uma operação matemática simples."""

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")

    operacao = input("Escolha a operação (+, -, *, /): ")

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            return
        else:
            resultado = num1 / num2
    else:
        print("Operação inválida.")
        return

    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")

if __name__ == "__main__":
    calculadora_simples()
