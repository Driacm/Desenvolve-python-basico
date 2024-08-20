def receber_lista(numero):
    lista = []
    print(f"Digite os números para a lista {numero} (digite 'sair' para finalizar):")
    while True:
        valor = input()
        if valor.lower() == 'sair':
            break
        try:
            numero = int(valor)
            lista.append(numero)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    return lista

def main():
    print("Bem-vindo! Vamos criar duas listas de números.")
    
    # Recebe as duas listas do usuário
    lista1 = receber_lista(1)
    lista2 = receber_lista(2)
    
    # Combina as duas listas
    lista_combinada = lista1 + lista2
    
    # Exibe as listas originais e a lista combinada
    print("\nLista 1:", lista1)
    print("Lista 2:", lista2)
    print("Lista combinada:", lista_combinada)

if __name__ == "__main__":
    main()
