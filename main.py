import os
from bettingGame import BettingGame

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_center(message):
    terminal_width = os.get_terminal_size().columns
    print(message.center(terminal_width))

def display_menu():
    clear_screen()
    print_center("Bem-vindo ao Jogo de Apostas!")
    print("\n1. Registrar jogador")
    print("2. Remover jogador")
    print("3. Fazer uma aposta")
    print("4. Ver saldo")
    print("5. Iniciar o jogo")
    print("6. Sair")

def main():
    game = BettingGame()
    while True:
        display_menu()
        choice = input("\nEscolha uma opção: ")
        
        if choice == '1':
            name = input("Digite o nome do jogador: ")
            balance = float(input("Digite o saldo inicial do jogador: "))
            game.add_player(name, balance)
            input("\nPressione Enter para continuar...")
        
        elif choice == '2':
            name = input("Digite o nome do jogador que deseja remover: ")
            game.remove_player(name)
            input("\nPressione Enter para continuar...")

        elif choice == '3':
            name = input("Digite o nome do jogador que deseja fazer a aposta: ")
            amount = float(input("Digite o valor da aposta: "))
            num = int(input("Digite o número em que deseja apostar (entre 1 e 5): "))
            game.place_bet(name, amount, num)
            input("\nPressione Enter para continuar...")
        
        elif choice == '4':
            clear_screen()
            print_center("Saldo dos jogadores:")
            for player, balance in game.players.items():
                print(f"{player}: ${balance:,.2f}")
            input("\nPressione Enter para continuar...")
        
        elif choice == '5':
            if len(game.player_bets) < 2:
                input("\nÉ necessário ter no mínimo duas apostas feitas por jogadores diferentes para iniciar o jogo! Pressione Enter para continuar...")
            else:
                clear_screen()
                print_center("Iniciando o jogo...")
                game.start_game()
                input("\nPressione Enter para continuar...")
        
        elif choice == '6':
            print("Obrigado por jogar!")
            break
        
        else:
            input("\nOpção inválida! Pressione Enter para continuar...")

if __name__ == "__main__":
    main()