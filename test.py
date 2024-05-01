import os

teste = {}

def game():
    
    while True:
        print("1.add nome e valor!")
        print("2.Decrementar valor")
        print("3.incrementar valor")
        print(f"\nDB:{teste}")
        choice = int(input("\nDigite:"))
        
        if choice == 1:
            name = input("name:")
            value = float(input("value:"))
            teste[name] = value
            print("dicionario atualizado!")
            input()
            os.system("cls")
            
        elif choice == 2:
            n1 = float(input("value:"))
            teste[name] -= n1
            print("Valor decrementado!")
            input()
            os.system("cls")
            
        elif choice == 3:
            n2 = float(input("value:"))
            teste[name] += n2
            print("Valor incrementado!")
            input()
            os.system("cls")    

game()        