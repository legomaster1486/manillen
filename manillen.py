import random
from tkinter.font import names

rode_kaarten = ("h70", "h80", "h90", "hJ1", "hQ2", "hK3", "hA4", "hM5", "r70", "r80", "r90", "rJ1", "rQ2", "rK3", "rA4", "rM5")
zwarte_kaarten = ("p70", "p80", "p90", "pJ1", "pQ2", "pK3", "pA4", "pM5", "k70", "k80", "k90", "kJ1", "kQ2", "kK3", "kA4", "kM5")
kaarten = (rode_kaarten, zwarte_kaarten)


numOfPlayers = int(input("How many players do you have?\n"))

class player:
    def __init__(self, name: str, deck: list):
        self.name = name
        self.deck = deck
    def __str__(self):
        return f"{self.name} with {self.deck}"
    def __repr__(self):
        return f"{self.name} with {self.deck}"

def translate_kaart(kaart: str, dictionary: dict):
    for key in dictionary.keys():
        if key in kaart:
            return dictionary[key]

def next_player(numOfPlayers: int, current_player: int):
    if current_player + 1 > numOfPlayers:
        current_player = 1
    else:
        current_player += 1
    return current_player

def fourPlayers(playerNames: list):
    players = [player(playerNames[0], []), player(playerNames[1], []), player(playerNames[2], []), player(playerNames[3], [])]
    # kaarten geven
    alle_kaarten = list(rode_kaarten + zwarte_kaarten)
    random.shuffle(alle_kaarten)
    for p in range(4):
        for i in range(8):
            num = random.randint(0, len(alle_kaarten) - 1)
            players[p].deck.append(alle_kaarten[num])
            alle_kaarten.remove(alle_kaarten[num])

    def game(players: list, max_points: int):
        score_t1 = 0
        score_t2 = 0
        print(players)
        while score_t1 < max_points and score_t2 < max_points:
            for i in range(4):
                print(f"{players[i].name} maakt troef")
                troef = input("Troef p(piekens), h(hartens), k(klavers), r(ruiten), zonder")
                if troef != "zonder":
                    kaarten_dict = {
                        f"{troef}7": 10,
                        f"{troef}8": 11,
                        f"{troef}9": 12,
                        f"{troef}J": 13,
                        f"{troef}Q": 14,
                        f"{troef}K": 15,
                        f"{troef}A": 16,
                        f"{troef}M": 17,
                        "7": 0,
                        "8": 1,
                        "9": 2,
                        "J": 3,
                        "Q": 4,
                        "K": 5,
                        "A": 6,
                        "M": 7,

                    }
                if troef == "p":
                    pass
                elif troef == "h":
                    pass
                elif troef == "k":
                    pass
                elif troef == "r":
                    pass
                elif troef == "zonder":
                    pass
                current_player = 1
                for j in range(8):
                    gelegde_kaarten = []
                    gelegde_kaarten_waarden = []
                    for k in range(4):
                        current_player = next_player(numOfPlayers, current_player)
                        kaart = input(f"{players[current_player - 1].name}, leg een kaart:\n")
                        gelegde_kaarten.append(kaart)
                    for i in range(len(gelegde_kaarten)):
                        gelegde_kaarten_waarden.append(translate_kaart(gelegde_kaarten[i], kaarten_dict))
                    print(gelegde_kaarten_waarden)





    game(players, 61)








if numOfPlayers == 2:
    pass
elif numOfPlayers == 3:
    pass
elif numOfPlayers == 4:
    p = list()
    for i in range(4):
        p.append(input(f"Name of player {i+1}:\n"))
    fourPlayers(p)
else:
    pass
