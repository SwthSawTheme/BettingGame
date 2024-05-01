import random


class BettingGame:
    
    
    def __init__(self):
        self.players = {}
        self.pot = 0.0
        self.current_bet = 0.0
        self.winning_number = random.randint(1,5)
        self.player_bets = {}
        self.num_bet = {}
        
    def add_player(self,name, opening_balance):
        if name not in self.players:
            self.players[name] = float(opening_balance)
        else:
            print("Jogador já registrado!")
    
    def remove_player(self,name):
        if name not in self.players:
            print("Jogador não encontrado!")
        else:
            del self.players[name]
    
    def place_bet(self,player,amount,num):
        if player in self.players and self.players[player] >= amount:
            self.players[player] -= amount
            self.player_bets[player] = amount
            self.num_bet[player] = num
            self.current_bet += amount
            self.pot += amount
            print(f"{player} apostou ${amount:.2f} dolares no número {num}")
        else:
            print(f"{player} está com saldo insuficiente!")
            
    def match_winner(self):
        num = self.winning_number
        return num
    
    def reset_game(self):
        self.players = {}
        self.pot = 0.0
        self.player_bets = {}
        self.num_bet = {}
            
    def start_game(self):
        result = self.winning_number
        winners = []
        
        for player,num in self.num_bet.items():
            if num == result:
                winners.append(player)
        
        if winners:
            pot = self.pot / len(winners)
            for winner in winners:
                self.players[winner] += pot
                print(f"{winner} venceu a rodada e ganhou ${pot:.2f}")
        else:
            print("Não teve ganhadores!")
            self.reset_game()
    
if __name__ == "__main__":
    cassino = BettingGame()
    
    cassino.add_player("Saw",20000)
    cassino.place_bet("Saw", 4000,3)
    cassino.add_player("Clary",30000)
    cassino.place_bet("Clary",5000,4)
    
    cassino.start_game()