# Neste algoritmo, crie uma variável que armazena varias string e sua quantidade.


print("Criar uma Lista de Comprar")
lista_strings = []
quantidades = []
contador = 0        

while True:
    item = input("Digite um item para a lista (ou 'sair' para finalizar): ")
    if item.lower() == 'sair':
        break
    quantidade = int(input(f"Digite a quantidade de '{item}': "))
    lista_strings.append(item)
    quantidades.append(quantidade)

    contador += 1

    
print("Itens na lista e suas quantidades:")
for item, qtd in zip(lista_strings, quantidades):
    print(f"{item}: {qtd}")

print("Quantidade total de itens:", sum(quantidades))