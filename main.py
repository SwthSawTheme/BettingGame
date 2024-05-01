from bettingGame import BettingGame
import os


def main():
    game = BettingGame()
    
    while True:
        os.system("cls")
        print(50*"▓","Cassino Offline",50*"▓")
        print("\n|"+"1.Jogar".center(115)+"|","\n|"+"2.Novo jogador".center(115)+"|","\n|"+"3.Remover jogador".center(115)+"|","\n|"+"4.Sair do jogo".center(115)+"|")
        print("\n|"+"Selecione um número e pressione enter...".center(115)+"|")
        
        choice = int(input(""))
        
        if choice == 1:
            game.start_game()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            break
main()