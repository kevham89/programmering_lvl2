import msvcrt

class game:
    def __init__(self, max_x, max_y, min_x, min_y, treasure_x, treasure_y):
        self.max_x = max_x
        self.min_x = min_x
        self.min_y = min_y
        self.max_y = max_y
        self.__treasure_x = treasure_x
        self.__treasure_y = treasure_y
    def check_treasure(self, player_posx, player_posy, player_name):
        if player_posx == self.__treasure_x and player_posy == self.__treasure_y:
            print(f"{player_name} hittade skatten! på x{player_posx}y{player_posy} ")
            return True
        return False
    def draw(self, players):
        for y in range(self.max_y, self.min_y -1, -1):
            row=""
            for x in range(self.min_x, self.max_x +1):
                cell = "."
                for p in players:
                    if p.player_posx == x and p.player_posy == y:
                        cell = p.name[0]
                row += cell + " "
            print(row)
        print()
class player:
    def __init__(self, name, player_posx, player_posy):
        self.name = name
        self.player_posx = player_posx
        self.player_posy = player_posy
    def movement(self, dx, dy, game1):
        new_x = self.player_posx +dx
        new_y = self.player_posy +dy
        if new_x < game1.min_x or new_x > game1.max_x:
            print(f"{self.name} kan inte gå utanför kartan, försök igen.")
            return
        if new_y < game1.min_y or new_y > game1.max_y:
            print(f"{self.name} kan inte gå utanför kartan, försök igen.")
            return
        self.player_posx = new_x
        self.player_posy = new_y
        print(f"{self.name} Din nya position är x{self.player_posx}y{self.player_posy}")
        game1.check_treasure(self.player_posx, self.player_posy, self.name)

game1 = game(max_x=5, max_y=5, min_x=0, min_y=0, treasure_x=3, treasure_y=3)

player1 = player("1Player", player_posx=0, player_posy=0)
player2 = player("2Player", player_posx=0, player_posy=0)

current_player = player1
while True:
    print(f"Nu spelar {current_player.name}")
    key = msvcrt.getch().decode('utf-8').lower()
    if key == "w":
        found = current_player.movement(0,1, game1)
        game1.draw([player1, player2])
    elif key == "s":
        found = current_player.movement(0, -1, game1)
        game1.draw([player1, player2])
    elif key == "a":
        found = current_player.movement(-1, 0, game1)
        game1.draw([player1, player2])
    elif key == "d":
        found = current_player.movement(1, 0, game1)
        game1.draw([player1, player2])
    elif key == "q":
        print("Avslutar spelet")
        break
    else:
        print("Okänd tangent.")
        continue
    current_player = player2 if current_player == player1 else player1
    