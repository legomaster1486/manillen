const rode_kaarten = ["h70", "h80", "h90", "hJ1", "hQ2", "hK3", "hA4", "hM5", "r70", "r80", "r90", "rJ1", "rQ2", "rK3", "rA4", "rM5"]
const zwarte_kaarten = ["p70", "p80", "p90", "pJ1", "pQ2", "pK3", "pA4", "pM5", "k70", "k80", "k90", "kJ1", "kQ2", "kK3", "kA4", "kM5"]
let numOfplayers = 0
let players = []
let playerNames = ["a", "b", "c", "d"]
// waarde van selectie lijst verkrijgen
function aantalSpelers(){
    numOfplayers = Number(document.querySelector(".aantalspelers").value)
}

// player object aanmaken
function player(name, deck, score) {
    this.name = name;
    this.deck = deck;
    this.score = score;
}


// waarde van kaart bepalen
function translate_kaart(kaart, waarden){
   for (let key of waarden.keys()){
    if (kaart.includes(key)){
        return waarden.get(key)
    }
   }
}

// volgende speler bepalen, 3+1 --> 0
function next_player(numOfplayers, currentPlayer){
    if (currentPlayer + 1 >= numOfplayers){currentPlayer = 0}
    else {currentPlayer ++ }
    return currentPlayer
}

function kaartendelen(playerNames){
    var allekaarten = rode_kaarten.concat(zwarte_kaarten)
    for (let i = 0; i < playerNames.length; i++){
        for (let j = 0; j < Math.floor(32/numOfplayers); j++){
            let num = Math.floor(Math.random() * -1 * (allekaarten.length -1))
            players[i].deck.push(allekaarten.at(num))
            allekaarten.splice(num, 1)
        }
    }
}

// spelers verschuiven om te bepalen wie er begint
function verschuiven(lijst){
    lijst.push(lijst.shift())
}

function max_points(){
    let max_points = 0
    for (let i = 0; i < numOfplayers; i++){
        if (max_points < players[i].score){
            max_points = players[i].score
        }
    }
    return max_points
}

// spel starten
function start(){
    if (numOfplayers == 0){
        document.querySelector(".error").innerHTML = "Kies eerst een waarde!"
    }
    else {
        players = []
        for (let i = 0; i < numOfplayers; i++){
        players.push(new player(playerNames[i], [], 0))
        //console.log(player[i].name + " " + player[i].deck + " " + player[i].score)
        }
        while (max_points() < 101){
            kaartendelen(playerNames)
            console.log(players)
            console.log(players[0].deck)
            console.log(`${players[0].name} maakt troef:`)
            troef = prompt("Troef p(piekens), h(hartens), k(klavers), r(ruiten) of zonder")
            kaarten_dict = new Map([
            [`${troef}7`, 10],
            [`${troef}8`, 11],
            [`${troef}9`, 12],
            [`${troef}J`, 13],
            [`${troef}Q`, 14],
            [`${troef}K`, 15],
            [`${troef}A`, 16],
            [`${troef}M`, 17],
            ["7", 0],
            ["8", 1],
            ["9", 2],
            ["J", 3],
            ["Q", 4],
            ["K", 5],
            ["A", 6],
            ["M", 7]
            ])

            // beginnende speler is degene na troefmaker
            let leggende_speler = 1
            for (let j = 0; j < players[0].deck.length; j++){
                let gelegde_kaarten = []
                let gelegde_kaarten_waarden = []

                // kaart leggen
                for (let k = 0; k < numOfplayers; k++){
                    var slagpunten = 0
                    console.log(players[leggende_speler].deck)
                    var kaart = prompt(`${players[leggende_speler].name}, leg een kaart: `)
                    while (!(players[leggende_speler].deck.includes(kaart))){
                        kaart = prompt(`${players[leggende_speler].name}, leg een kaart die je wel hebt!: `)
                    }
                    players[leggende_speler].deck.splice(players[leggende_speler].deck.indexOf(kaart), 1)
                    gelegde_kaarten.push([kaart, leggende_speler])
                    console.log(players[leggende_speler].deck)
                    leggende_speler = next_player(numOfplayers, leggende_speler)
                }
                // waardes van kaarten toevoegen die volgen of troef zijn
                for (let k = 0; k < gelegde_kaarten.length; k++){
                    if (gelegde_kaarten[k][0][0] == gelegde_kaarten[0][0][0] || gelegde_kaarten[k][0][0] == troef){
                        gelegde_kaarten_waarden.push([gelegde_kaarten[k][0], translate_kaart(gelegde_kaarten[k][0], kaarten_dict)])
                    }
                }

                // slagpunten bepalen
                for (let k of gelegde_kaarten){
                    slagpunten += Number(k[0][2])
                }
                // zoeken naar hoogste kaart
                var hoogste_kaart = ["", 0]
                console.log("Hoogste kaart:")
                for (k of gelegde_kaarten_waarden){
                    if (k[1] >= hoogste_kaart[1]){
                        hoogste_kaart = k
                    }
                console.log(hoogste_kaart)
                }

                // punten bepalen
                console.log("Gelegde kaarten:")
                for (let k of gelegde_kaarten){
                    console.log(k)
                    if (k[0] == hoogste_kaart[0]){
                        // speler die hoogste kaart heeft gelegd begint de volgende slag
                        leggende_speler = k[1]
                        // punten bij 3 spelers
                        if (numOfplayers == 3){
                            if (k[1] == 0){
                                players[0].score += slagpunten
                            }
                        }
                        if (numOfplayers % 2 == 0){
                            if (k[1] % 2 == 0){
                                for (let i = 0; i < numOfplayers; i += 2){
                                    players[i].score += slagpunten
                                }  
                            }
                            else {
                                for (let i = 0; i < numOfplayers; i += 2){
                                    players[i + 1].score += slagpunten
                                }
                            }
                        }
                    }
                }
                for (let k = 0; k < numOfplayers; k++){
                    console.log(players[k].score)
                }
            }
            verschuiven(players)
        }
    }
}
