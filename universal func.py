import random
class player:
    def __init__(self, name: str, deck: list, score: int):
        self.name = name
        self.deck = deck
        self.score = score
    def __str__(self):
        return f"{self.name} with {self.deck} and a score of {self.score}"
    def __repr__(self):
        return f"{self.name} with {self.deck} and a score of {self.score}"

numOfPlayers = int(input("How many players do you have?\n"))
rode_kaarten = ("h70", "h80", "h90", "hJ1", "hQ2", "hK3", "hA4", "hM5", "r70", "r80", "r90", "rJ1", "rQ2", "rK3", "rA4", "rM5")
zwarte_kaarten = ("p70", "p80", "p90", "pJ1", "pQ2", "pK3", "pA4", "pM5", "k70", "k80", "k90", "kJ1", "kQ2", "kK3", "kA4", "kM5")
kaarten = (rode_kaarten, zwarte_kaarten)


def next_player(numOfPlayers: int, current_player: int):
    if current_player + 1 >= numOfPlayers:
        current_player = 0
    else:
        current_player += 1
    return current_player


def translate_kaart(kaart: str, dictionary: dict):
    for key in dictionary.keys():
        if key in kaart:
            return dictionary[key]


def kaartendelen(playerNames: list):
    alle_kaarten = list(rode_kaarten + zwarte_kaarten)
    random.shuffle(alle_kaarten)
    for p in range(len(playerNames)):
        for i in range(32 // numOfPlayers):
            num = random.randint(0, len(alle_kaarten) - 1)
            players[p].deck.append(alle_kaarten[num])
            alle_kaarten.remove(alle_kaarten[num])


def verschuif_lijst(lijst: list):
    for i in range(len(lijst)):
        lijst.insert(i - 1, lijst[i])
        lijst.pop(i)


p = ["a", "b", "c", "d"]
players = []
for i in p:
    players.append(player(i, [], 0))




def game(max_score: int):
    while max([i.score for i in players]) < max_score:
        kaartendelen(p)
        print(players)
        print(f"{players[0].name} maakt troef:")
        troef = input("Troef p(piekens), h(hartens), k(klavers), r(ruiten), zonder\n")
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

        for j in range(len(players[0].deck)):
            print(players)
            gelegde_kaarten = []
            gelegde_kaarten_waarden = []
            # kaart leggen
            leggende_speler = 1
            for k in range(numOfPlayers):
                slagpunten = 0
                print(leggende_speler, "begin")
                kaart = input(f"{players[leggende_speler].name}, leg een kaart:\n")
                while kaart not in players[leggende_speler].deck:
                    kaart = input(f"{players[leggende_speler].name}, leg een kaart die je hebt:\n")
                players[leggende_speler].deck.remove(kaart)
                gelegde_kaarten.append((kaart, leggende_speler))
                leggende_speler = next_player(numOfPlayers, leggende_speler)
            # kaart waarde toegeven voor computer
            for k in range(len(gelegde_kaarten)):
                if gelegde_kaarten[0][0][0] == gelegde_kaarten[k][0][0] or gelegde_kaarten[k][0][0] == troef:
                    gelegde_kaarten_waarden.append((translate_kaart(gelegde_kaarten[k][0], kaarten_dict), gelegde_kaarten[k][0]))
            # zkn naar hoogste kaart uit slag
            for k in gelegde_kaarten_waarden:
                if k[0] == max([x[0] for x in gelegde_kaarten_waarden]):
                    highest_card = k[1]
            # aantal ptn in slag berekenen
            for k in gelegde_kaarten:
                slagpunten += int(k[0][2])
            print(players)

            for k, l in gelegde_kaarten:
                if k == highest_card:
                    # punten bij 3 spelers
                    if numOfPlayers == 3:
                        if l == 0:
                            players[0].score += slagpunten
                        else:
                            players[1].score += slagpunten
                            players[2].socre += slagpunten
                    # punten bij 4 of 2 spelers
                    if numOfPlayers % 2 == 0:
                        if l % 2 == 0:
                            for i in range(0, numOfPlayers, 2):
                                players[i].score += slagpunten
                        else:
                            for i in range(0, numOfPlayers, 2):
                                players[i + 1].score += slagpunten
            verschuif_lijst(players)
game(100)