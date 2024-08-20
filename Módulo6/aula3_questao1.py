def solicitar_numeros():
    numeros = []

    # Solicita pelo menos 4 números do usuário
    while len(numeros) < 4:
        try:
            numero = int(input("Digite um número inteiro (ou 'sair' para finalizar): "))
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    # Permite ao usuário adicionar mais números, se quiser
    while True:
        continuar = input("Deseja adicionar mais números? (s/n): ").strip().lower()
        if continuar == 's':
            try:
                numero = int(input("Digite um número inteiro: "))
                numeros.append(numero)
            except ValueError:
                print("Por favor, digite um número inteiro válido.")
        elif continuar == 'n':
            break
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")

    return numeros

def exibir_fatiamentos(numeros):
    print(f"Lista original: {numeros}")
    print(f"Três primeiros elementos: {numeros[:3]}")
    print(f"Dois últimos elementos: {numeros[-2:]}")
    print(f"Lista invertida: {numeros[::-1]}")
    print(f"Elementos de índice par: {numeros[::2]}")
    print(f"Elementos de índice ímpar: {numeros[1::2]}")

def main():
    numeros = solicitar_numeros()
    exibir_fatiamentos(numeros)

if __name__ == "__main__":
    main()

