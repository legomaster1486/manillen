const rode_kaarten = ["h70", "h80", "h90", "hJ1", "hQ2", "hK3", "hA4", "hM5", "r70", "r80", "r90", "rJ1", "rQ2", "rK3", "rA4", "rM5"]
const zwarte_kaarten = ["p70", "p80", "p90", "pJ1", "pQ2", "pK3", "pA4", "pM5", "k70", "k80", "k90", "kJ1", "kQ2", "kK3", "kA4", "kM5"]

function aantalSpelers(){
    let numOfplayers = Number(document.querySelector(".aantalspelers").value)
    console.log(numOfplayers)
    if (isNaN(numOfplayers) || !(2 <= numOfplayers && numOfplayers <= 4)){
        document.querySelector(".antwoord").innerHTML = "Opties: 2, 3 of 4"
    }
    else{
        document.querySelector(".antwoord").innerHTML = `OK, er zijn ${numOfplayers} spelers`
    }
}
