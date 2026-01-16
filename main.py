print("Movimentação das Peças de Xadrez")
print("1 - Torre")
print("2 - Bispo")
print("3 - Cavalo")
print("4 - Rainha")
print("5 - Rei")

opcao = input("Escolha a peça: ")

if opcao == "1":
    print("Torre: movimenta-se em linha reta (horizontal e vertical).")
elif opcao == "2":
    print("Bispo: movimenta-se em diagonais.")
elif opcao == "3":
    print("Cavalo: movimenta-se em L.")
elif opcao == "4":
    print("Rainha: movimenta-se em linhas retas e diagonais.")
elif opcao == "5":
    print("Rei: movimenta-se uma casa em qualquer direção.")
else:
    print("Opção inválida.")
