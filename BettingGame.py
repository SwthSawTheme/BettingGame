import random


class BettingGame:
    
    
    def __init__(self):
        self.players = {}
        self.pot = 0.0
        self.current_bet = 0.0
        self.winning_number = None
        self.player_bets = {}
        
    def add_player(self,name, opening_balance):
        if name not in self.players:
            self.players[name] = opening_balance
        else:
            print("Jogador já registrado!")
    
    def remove_player(self,name):
        if name not in self.players:
            print("Jogador não encontrado!")
        else:
            del self.players[name]
    
    def place_bet(self,player,amount):
        if player in self.players and amount >= self.players[player]:
            self.players[player] -= amount
            self.player_bets[player] = amount
            self.current_bet += amount
            print(f"{player} apostou ${amount:.2f}")
        else:
            print("Saldo insuficiente, ou jogador não registrado!")
    
    def num_aposta(self):
        self.winning_number = random.randint(1.5)
        for player in self.players:
            num = int(input("Escolha um número: "))
            
        
    
    def start_game(self):
        if len(self.player_bets) >= 2:
            for player, value in self.player_bets:
                self.pot += value

        else:
            print("Necessário 2 jogadores no minimo para iniciar!")
    
    def match_winner(self):
        pass
    
    def reset_game(self):
        pass